# app/routes/main.py
"""
Rutas principales y endpoints de API para SalsaQuest.
Maneja la navegación general y las respuestas JSON para la línea de tiempo y trivias.
"""

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


@main_bp.route('/api/trivia')
def get_trivia():
    """Retorna las preguntas y opciones para el módulo de trivia/desafío."""
    preguntas = [
        {
            "id": 1,
            "pregunta": "¿En qué década comenzó a consolidarse el término 'Salsa' en Nueva York?",
            "opciones": ["1950", "1960 - 1970", "1990", "2000"],
            "correcta": 1
        },
        {
            "id": 2,
            "pregunta": "¿Qué famosa orquesta neoyorquina reunió a grandes figuras como Celia Cruz, Willie Colón y Héctor Lavoe?",
            "opciones": ["Fania All-Stars", "El Gran Combo", "Sonora Matancera", "Grupo Niche"],
            "correcta": 0
        },
        {
            "id": 3,
            "pregunta": "¿Qué instrumento es considerado la columna vertebral del ritmo en la salsa?",
            "opciones": ["El Piano", "El Bajo", "La Clave", "El Saxofón"],
            "correcta": 2
        }
    ]
    return jsonify(preguntas)