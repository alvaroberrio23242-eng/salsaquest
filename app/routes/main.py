# app/routes/main.py
from flask import Blueprint, render_template, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/desafio')
def desafio():
    return render_template('desafio.html')

@main_bp.route('/api/trivia', methods=['GET'])
def get_trivia():
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

# NOTA: la ruta /api/leaderboard (GET publico y POST de captura de lead)
# vive SOLO en app/routes/auth.py. Antes tambien estaba definida aqui,
# duplicada con distinto comportamiento (esta version devolvia solo
# username/score; la de auth.py exponia email/whatsapp en el GET) — dos
# blueprints registrando la misma URL+metodo es ambiguo, asi que se
# unifico en un unico lugar.