# app/routes/main.py
"""
Rutas principales y endpoints de API para SalsaQuest.
Maneja la navegación general, la línea de tiempo, las trivias y el leaderboard.
"""

from flask import Blueprint, render_template, jsonify, request
from app import db
from app.models.timeline_data import TimelineData
from app.models.user import User

# Definición del Blueprint principal
main_bp = Blueprint('main', __name__)


# ==========================================
# RUTAS DE VISTAS (HTML)
# ==========================================

@main_bp.route('/')
def index():
    """Sirve la página principal."""
    return render_template('index.html')


@main_bp.route('/desafio')
def desafio():
    """Ruta para cargar la vista del desafío / trivia."""
    return render_template('desafio.html')


# ==========================================
# ENDPOINTS DE LA API (JSON)
# ==========================================

@main_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    """Consulta los eventos de la base de datos y los retorna en formato JSON."""
    try:
        eventos = TimelineData.query.all()
        return jsonify([evento.to_dict() for evento in eventos])
    except Exception as e:
        print(f"Error al consultar la BD para el timeline: {e}")
        return jsonify([]), 500


@main_bp.route('/api/timeline', methods=['POST'])
def add_timeline_event():
    """Guarda un nuevo hito enviado desde el formulario."""
    try:
        data = request.json or {}
        nuevo_evento = TimelineData(
            anio=data.get('anio'),
            titulo=data.get('titulo'),
            descripcion=data.get('descripcion'),
            trivia=data.get('trivia'),
            imagen_url=data.get('imagen_url')
        )
        db.session.add(nuevo_evento)
        db.session.commit()
        return jsonify({"message": "Evento guardado"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@main_bp.route('/api/trivia', methods=['GET'])
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


@main_bp.route('/api/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    """Consulta (GET) y guarda (POST) las puntuaciones del quiz."""
    if request.method == 'POST':
        try:
            data = request.json or {}
            nombre = data.get('nombre_jugador', 'Jugador Anónimo')
            puntaje = data.get('puntaje', 0)
            
            user = User.query.filter_by(username=nombre).first()
            if not user:
                user = User(username=nombre, score=puntaje)
                db.session.add(user)
            else:
                if puntaje > user.score:
                    user.score = puntaje
            
            db.session.commit()
            return jsonify({"message": "Puntuación guardada"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    # GET: Obtener el top 5 de jugadores
    jugadores = User.query.order_by(User.score.desc()).limit(5).all()
    return jsonify([{"username": u.username, "score": u.score} for u in jugadores])