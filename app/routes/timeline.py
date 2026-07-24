# app/routes/timeline.py
"""
Rutas específicas para la gestión y consulta de la línea de tiempo.
"""

from flask import Blueprint, jsonify, request
from app import db
from app.models.timeline_data import TimelineData

timeline_bp = Blueprint('timeline', __name__)


@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    """Retorna todos los eventos de la línea de tiempo."""
    try:
        eventos = TimelineData.query.all()
        return jsonify([evento.to_dict() for evento in eventos]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@timeline_bp.route('/api/timeline', methods=['POST'])
def add_timeline_event():
    """Agrega un nuevo hito a la línea de tiempo."""
    try:
        data = request.json or {}
        nuevo_evento = TimelineData(
            anio=data.get('anio'),
            titulo=data.get('titulo'),
            descripcion=data.get('descripcion'),
            trivia=data.get('trivia'),
            imagen_url=data.get('imagen_url'),
            audio_url=data.get('audio_url')
        )
        db.session.add(nuevo_evento)
        db.session.commit()
        return jsonify({"message": "Evento guardado con éxito"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500