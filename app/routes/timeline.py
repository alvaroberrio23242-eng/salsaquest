# app/routes/timeline.py

"""
Rutas relacionadas con la línea de tiempo de SalsaQuest.
"""

from flask import Blueprint, jsonify
from app.models.timeline_data import obtener_todos_los_nodos, obtener_nodo_por_id

# Un Blueprint es un "mini paquete de rutas" que luego registramos en la app principal.
# Así separamos las rutas por tema (timeline, usuarios, ventas, etc.) en vez de un solo archivo.
timeline_bp = Blueprint('timeline', __name__)


@timeline_bp.route('/api/timeline', methods=['GET'])
def obtener_timeline():
    """Devuelve todos los nodos de la línea de tiempo en formato JSON."""
    nodos = obtener_todos_los_nodos()
    return jsonify(nodos)


@timeline_bp.route('/api/timeline/<int:nodo_id>', methods=['GET'])
def obtener_nodo(nodo_id):
    """Devuelve un solo nodo por su id."""
    nodo = obtener_nodo_por_id(nodo_id)
    if nodo is None:
        return jsonify({"error": "Nodo no encontrado"}), 404
    return jsonify(nodo)