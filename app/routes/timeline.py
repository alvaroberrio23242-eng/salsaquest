from flask import Blueprint, jsonify

from app import db
from app.models.timeline_data import TimelineData
from app.models.timeline_events_data import (
    COLUMNAS_MODELO,
    EVENTOS_TIMELINE,
    _anio_numerico,
    credito_por_titulo,
    filtrar_columnas,
)
import re

timeline_bp = Blueprint('timeline', __name__)

# Datos semilla: se insertan UNA sola vez (solo si la tabla esta vacia).
# Antes, este endpoint borraba y volvia a insertar estos eventos en
# CADA visita a la pagina -- en SQLite esto podia chocar como
# "database is locked" y mostrar "Error al cargar".

_ID_VIDEO_RE = re.compile(r"/embed/([\w-]+)")

# IDs de video que existen (verificados via oEmbed de YouTube). Cualquier
# audio_url en BD cuyo ID no este aqui es un residuo del dataset viejo
# (7 IDs inventados que devolvian 404) y se neutraliza al hacer backfill.
_IDS_VIDEO_VALIDOS = {
    _ID_VIDEO_RE.search(e["audio_url"]).group(1)
    for e in EVENTOS_TIMELINE
    if e.get("audio_url")
}

_TITULOS_CANONICOS = {e["titulo"] for e in EVENTOS_TIMELINE}

# Titulos del dataset antiguo (init_db.py pre-canonico) que fueron
# reemplazados por un hito canonico equivalente y mejor documentado.
# Limpieza explicita y acotada a esta lista: nunca se borra nada fuera
# de aqui (los datos que agregue un admin o un usuario se respetan).
_TITULOS_OBSOLETOS = {
    "Son Cubano",
    "Nacimiento de Fania Records",
    "Debut de Willie Colón y Héctor Lavoe",
    "Celia Cruz & Fania en África",
    "Lanzamiento de 'Siembra'",
    "Grupo Niche & Jairo Varela",
    "La Timba Cubana: Los Van Van",
}


def sembrar_eventos_faltantes():
    """Siembra canonica idempotente:
    - tabla vacia -> inserta EVENTOS_TIMELINE completo;
    - tabla con datos legados -> agrega SOLO los hitos canonicos que
      falten (match por titulo), neutraliza audio_url con IDs de video
      inexistentes y elimina las filas legadas obsoletas declaradas en
      _TITULOS_OBSOLETOS. Nunca borra nada fuera de esa lista."""
    if TimelineData.query.count() == 0:
        for datos in EVENTOS_TIMELINE:
            db.session.add(TimelineData(**filtrar_columnas(datos)))
        db.session.commit()
        return

    titulos_existentes = {t[0] for t in db.session.query(TimelineData.titulo).all()}
    faltantes = [
        e for e in EVENTOS_TIMELINE if e["titulo"] not in titulos_existentes
    ]
    for datos in faltantes:
        db.session.add(TimelineData(**filtrar_columnas(datos)))

    # Residuos del dataset antiguo: videos que ya no existen (404).
    invalidos = (
        TimelineData.query.filter(TimelineData.audio_url.isnot(None)).all()
    )
    for fila in invalidos:
        m = _ID_VIDEO_RE.search(fila.audio_url or "")
        if not m or m.group(1) not in _IDS_VIDEO_VALIDOS:
            fila.audio_url = None

    # Filas legadas sustituidas por hitos canonicos.
    if _TITULOS_OBSOLETOS & titulos_existentes:
        TimelineData.query.filter(
            TimelineData.titulo.in_(_TITULOS_OBSOLETOS)
        ).delete(synchronize_session=False)

    db.session.commit()


@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        sembrar_eventos_faltantes()

        # Orden cronologico NUMERICO en Python (los anios son strings,
        # pueden ser rangos como "1900-1940"; el orden SQL .asc() es
        # alfabetico y rompe con formatos mixtos).
        filas = sorted(
            TimelineData.query.all(),
            key=lambda e: (_anio_numerico(e.anio), e.titulo),
        )

        return jsonify([
            {**e.to_dict(),
             "imagen_credito": credito_por_titulo(e.titulo)}
            for e in filas
        ])

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
