# app/routes/content.py
from flask import Blueprint, jsonify
from app.models.content_data import (
    GRANDES_EVENTOS, RECORDS_SALSA, ARTISTAS, TIMBA, ENTREVISTAS, CARATULAS_ICONICAS,
    ORQUESTAS, INSTRUMENTOS, MUSEOS_SALSA, LUGARES_SALSEROS, RANKING_ALBUMES, RANKING_FUENTE_URL,
    MEDELLIN_HISTORIA, MEDELLIN_BARES, MEDELLIN_EMISORAS, MEDELLIN_PLAYLIST_URL, MEDELLIN_PENDIENTE,
    MEDELLIN_EVENTOS, MEDELLIN_CALENDARIO_VIVO_URL, GRAMMY_SALSA, FOTOS_VALIDADAS
)
from app.models.visit_counter import VisitCounter

content_bp = Blueprint('content', __name__)


@content_bp.route('/api/eventos-grandes', methods=['GET'])
def get_eventos_grandes():
    return jsonify(GRANDES_EVENTOS)


@content_bp.route('/api/records-salsa', methods=['GET'])
def get_records_salsa():
    return jsonify(RECORDS_SALSA)


@content_bp.route('/api/artistas', methods=['GET'])
def get_artistas():
    return jsonify(ARTISTAS)


@content_bp.route('/api/artistas/<slug>', methods=['GET'])
def get_artista(slug):
    artista = next((a for a in ARTISTAS if a['slug'] == slug), None)
    if artista is None:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify(artista)


@content_bp.route('/api/timba', methods=['GET'])
def get_timba():
    return jsonify(TIMBA)


@content_bp.route('/api/entrevistas', methods=['GET'])
def get_entrevistas():
    return jsonify(ENTREVISTAS)


@content_bp.route('/api/caratulas', methods=['GET'])
def get_caratulas():
    return jsonify(CARATULAS_ICONICAS)


@content_bp.route('/api/orquestas', methods=['GET'])
def get_orquestas():
    return jsonify(ORQUESTAS)


@content_bp.route('/api/instrumentos', methods=['GET'])
def get_instrumentos():
    return jsonify(INSTRUMENTOS)


@content_bp.route('/api/museos', methods=['GET'])
def get_museos():
    return jsonify(MUSEOS_SALSA)


@content_bp.route('/api/lugares-salseros', methods=['GET'])
def get_lugares_salseros():
    return jsonify(LUGARES_SALSEROS)


@content_bp.route('/api/ranking-albumes', methods=['GET'])
def get_ranking_albumes():
    return jsonify({"fuente_url": RANKING_FUENTE_URL, "albumes": RANKING_ALBUMES})


@content_bp.route('/api/medellin', methods=['GET'])
def get_medellin():
    return jsonify({
        "historia": MEDELLIN_HISTORIA,
        "bares": MEDELLIN_BARES,
        "emisoras": MEDELLIN_EMISORAS,
        "playlist_url": MEDELLIN_PLAYLIST_URL,
        "eventos": MEDELLIN_EVENTOS,
        "calendario_vivo_url": MEDELLIN_CALENDARIO_VIVO_URL,
        "pendiente": MEDELLIN_PENDIENTE,
    })


@content_bp.route('/api/grammy', methods=['GET'])
def get_grammy():
    return jsonify(GRAMMY_SALSA)


@content_bp.route('/api/fotos-artista/<slug>', methods=['GET'])
def get_fotos_artista(slug):
    """Galeria de fotos reales verificadas (Wikimedia Commons) para un
    artista, ademas de la imagen_url principal que ya trae ARTISTAS."""
    return jsonify(FOTOS_VALIDADAS.get(slug, []))


@content_bp.route('/api/visitas', methods=['GET'])
def get_visitas():
    try:
        total = VisitCounter.incrementar_y_obtener()
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
