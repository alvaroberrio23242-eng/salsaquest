# app/routes/timeline.py

import random
from flask import Blueprint, jsonify, request
from app import db
from app.models.timeline_data import Evento, UsuarioProgreso

timeline_bp = Blueprint('timeline', __name__)


# 1. Obtener todos los eventos (GET)
@timeline_bp.route('/api/timeline', methods=['GET'])
def obtener_timeline():
    """Devuelve todos los eventos ordenados por año."""
    eventos = Evento.query.order_by(Evento.anio.asc()).all()
    return jsonify([evento.to_dict() for evento in eventos])


# 2. Obtener dato curioso / trivia de un evento (GET)
@timeline_bp.route('/api/timeline/<int:nodo_id>/trivia', methods=['GET'])
def obtener_trivia(nodo_id):
    """Devuelve el dato curioso del evento consultado desde la BD."""
    evento = Evento.query.get(nodo_id)
    if evento and evento.dato_curioso:
        return jsonify({"dato_curioso": evento.dato_curioso})
    return jsonify({"dato_curioso": "La salsa es un género lleno de ritmo e historia."}), 200


# 3. Crear un nuevo evento (POST)
@timeline_bp.route('/api/timeline', methods=['POST'])
def crear_evento():
    """Crea un nuevo evento en la base de datos con imagen y audio."""
    data = request.get_json()

    if not data or not data.get('anio') or not data.get('titulo') or not data.get('descripcion'):
        return jsonify({"error": "Faltan datos requeridos (anio, titulo, descripcion)"}), 400

    nuevo_evento = Evento(
        era=data.get('era', 'raices'),
        anio=data['anio'],
        anio_fin=data.get('anio_fin'),
        titulo=data['titulo'],
        descripcion=data['descripcion'],
        dato_curioso=data.get('dato_curioso', ''),
        imagen_url=data.get('imagen_url', ''),
        audio_url=data.get('audio_url', '')
    )

    db.session.add(nuevo_evento)
    db.session.commit()

    return jsonify({
        "mensaje": "¡Evento creado con éxito!",
        "evento": nuevo_evento.to_dict()
    }), 201


# 4. Eliminar un evento (DELETE)
@timeline_bp.route('/api/timeline/<int:nodo_id>', methods=['DELETE'])
def eliminar_evento(nodo_id):
    """Elimina un evento de la base de datos."""
    evento = Evento.query.get(nodo_id)
    if not evento:
        return jsonify({"error": "El evento no existe."}), 404

    db.session.delete(evento)
    db.session.commit()

    return jsonify({"mensaje": f"Evento {nodo_id} eliminado con éxito."}), 200


# 5. Generar pregunta aleatoria para el Quiz (GET)
@timeline_bp.route('/api/quiz/pregunta', methods=['GET'])
def obtener_pregunta_quiz():
    """Genera una pregunta tipo opción múltiple basada en la BD."""
    eventos = Evento.query.all()
    if len(eventos) < 3:
        return jsonify({"error": "Se necesitan al menos 3 eventos en la BD para jugar."}), 400

    correcto = random.choice(eventos)
    otros_eventos = [e for e in eventos if e.id != correcto.id]
    distractores = random.sample(otros_eventos, min(2, len(otros_eventos)))

    opciones = [
        {"id": correcto.id, "anio": correcto.anio, "es_correcta": True},
        {"id": distractores[0].id, "anio": distractores[0].anio, "es_correcta": False},
        {"id": distractores[1].id, "anio": distractores[1].anio, "es_correcta": False}
    ]
    random.shuffle(opciones)

    return jsonify({
        "pregunta": f"¿En qué año ocurrió: '{correcto.titulo}'?",
        "descripcion": correcto.descripcion,
        "opciones": opciones
    })


# 6. Guardar o actualizar puntaje (POST)
@timeline_bp.route('/api/quiz/puntaje', methods=['POST'])
def guardar_puntaje():
    """Guarda o incrementa los puntos de un jugador."""
    data = request.get_json()
    nombre = data.get('nombre_jugador', 'Salsero Anónimo')
    puntos = data.get('puntaje', 0)

    jugador = UsuarioProgreso.query.filter_by(nombre_jugador=nombre).first()
    if jugador:
        jugador.puntaje += puntos
    else:
        jugador = UsuarioProgreso(nombre_jugador=nombre, puntaje=puntos)
        db.session.add(jugador)

    db.session.commit()
    return jsonify({"mensaje": "Puntaje guardado", "jugador": jugador.to_dict()}), 200


# 7. Obtener los mejores puntajes (GET)
@timeline_bp.route('/api/quiz/leaderboard', methods=['GET'])
def obtener_leaderboard():
    """Devuelve los 5 mejores jugadores."""
    mejores_jugadores = UsuarioProgreso.query.order_by(UsuarioProgreso.puntaje.desc()).limit(5).all()
    return jsonify([j.to_dict() for j in mejores_jugadores])