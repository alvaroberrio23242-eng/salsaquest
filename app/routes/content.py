# app/routes/content.py
from flask import Blueprint, jsonify
from app.models.content_data import GRANDES_EVENTOS, RECORDS_SALSA, ARTISTAS, TIMBA
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


@content_bp.route('/api/visitas', methods=['GET'])
def get_visitas():
    try:
        total = VisitCounter.incrementar_y_obtener()
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
