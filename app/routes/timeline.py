from flask import Blueprint, jsonify
from app.models.timeline_data import TimelineData
from app import db

timeline_bp = Blueprint('timeline', __name__)

# Datos semilla: se insertan UNA sola vez (solo si la tabla esta vacia).
# Antes, este endpoint borraba y volvia a insertar estos 4 eventos en
# CADA visita a la pagina (db.session.query(TimelineData).delete()),
# lo que ademas se disparaba DOS VECES por carga de pagina (timeline.js
# Y content.js pedian /api/timeline por separado) -- en SQLite esto
# podia chocar como "database is locked" y mostrar "Error al cargar".
_EVENTOS_SEMILLA = [
    dict(
        anio="1967",
        titulo="El Malo",
        artista="Willie Colón",
        descripcion="Álbum debut de Willie Colón, grabado a los 17 años, con un joven Héctor Lavoe de 21: el inicio del sonido 'duro' de la salsa neoyorquina.",
        trivia="Fue la primera colaboración entre Colón y Lavoe, una de las duplas más influyentes de la historia de la salsa.",
        spotify_album_id="6ROTUtQlp130rdHDff3nhE",
    ),
    dict(
        anio="1974",
        titulo="Celia & Johnny",
        artista="Celia Cruz & Johnny Pacheco",
        descripcion="Consagró a Celia Cruz como reina de la salsa tras su exilio de Cuba, con 'Quimbara' como himno.",
        trivia="En 2014 la Biblioteca del Congreso de EE. UU. lo declaró de importancia histórica y cultural.",
        spotify_album_id="416lPCtckkTOPYQslZ6QH1",
    ),
    dict(
        anio="1975",
        titulo="Live At Yankee Stadium, Vol. 1",
        artista="Fania All-Stars",
        descripcion="Registro en vivo de uno de los conciertos más grandes que ha tenido la salsa como movimiento masivo.",
        trivia="Grabado en el legendario estadio de béisbol de Nueva York, con 'Mi Gente' entre sus temas centrales.",
        spotify_album_id="2W5VinmurxO8g1QgKN5j4P",
    ),
    dict(
        anio="1977",
        titulo="Metiendo Mano!",
        artista="Willie Colón & Rubén Blades",
        descripcion="Primer álbum de la dupla Colón-Blades, un año antes de 'Siembra'.",
        trivia="'Pablo Pueblo' es considerado uno de los primeros pasos hacia la salsa 'consciente', con letras de crítica social.",
        spotify_album_id="4aagt0vBz9fm14XaYzlOdL",
    ),
    dict(
        anio="1978",
        titulo="Siembra",
        artista="Willie Colón & Rubén Blades",
        descripcion="El álbum de salsa más vendido de la historia, con más de 3 millones de copias.",
        trivia="'Pedro Navaja' está inspirado en 'Mack the Knife' de Bertolt Brecht; el sello no quería incluirlo por ser 'muy largo'.",
        spotify_album_id="7wOJ9RTQr05ytqROWtTPzy",
    ),
]


@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        # Solo siembra los datos si la tabla esta realmente vacia (primera
        # vez que corre la app). Ya NO borra nada en cada peticion.
        if TimelineData.query.count() == 0:
            for datos in _EVENTOS_SEMILLA:
                db.session.add(TimelineData(**datos))
            db.session.commit()

        eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()
        return jsonify([e.to_dict() for e in eventos])

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
