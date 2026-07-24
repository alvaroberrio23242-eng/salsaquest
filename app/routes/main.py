# app/routes/main.py

from flask import Blueprint, render_template, jsonify
from app.models.timeline_data import TimelineData

# Definición del Blueprint principal
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Sirve la página principal."""
    return render_template('index.html')


@main_bp.route('/desafio')
def desafio():
    """Ruta para cargar la vista del desafío / trivia."""
    return render_template('desafio.html')


@main_bp.route('/api/timeline')
def get_timeline():
    """Consulta los eventos de la base de datos y los retorna en formato JSON para timeline.js."""
    try:
        eventos = TimelineData.query.all()
        return jsonify([evento.to_dict() for evento in eventos])
    except Exception as e:
        print(f"Error al consultar la BD para el timeline: {e}")
        return jsonify([]), 500