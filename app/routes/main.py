# app/routes/main.py
from flask import Blueprint, render_template, jsonify

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html', active_page='inicio')


@main_bp.route('/desafio')
def desafio():
    return render_template('desafio.html', active_page='inicio')


# ==========================================
# PÁGINAS DE CONTENIDO (arquitectura multipágina)
# ==========================================

@main_bp.route('/historia/linea-de-tiempo')
def historia_linea_de_tiempo():
    return render_template('historia_linea_de_tiempo.html', active_page='timeline')


@main_bp.route('/historia/eventos-y-records')
def historia_eventos_y_records():
    return render_template('historia_eventos_y_records.html', active_page='eventos_records')


@main_bp.route('/artistas')
def artistas():
    return render_template('artistas.html', active_page='artistas')


@main_bp.route('/musica/caratulas-y-albumes')
def musica_caratulas_y_albumes():
    return render_template('musica_caratulas_y_albumes.html', active_page='caratulas_albumes')


@main_bp.route('/musica/orquestas-e-instrumentos')
def musica_orquestas_e_instrumentos():
    return render_template('musica_orquestas_e_instrumentos.html', active_page='orquestas_instrumentos')


@main_bp.route('/lugares')
def lugares():
    return render_template('lugares.html', active_page='lugares')


@main_bp.route('/medellin')
def medellin():
    return render_template('medellin.html', active_page='medellin')


@main_bp.route('/premios-y-entrevistas')
def premios_y_entrevistas():
    return render_template('premios_y_entrevistas.html', active_page='premios_entrevistas')


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

# NOTA: la ruta /api/leaderboard (GET y POST) se quito de aqui. Vivia
# duplicada tambien en app/routes/auth.py con distinta logica (esa si
# guarda el registro/lead en la base de datos), y al haber dos rutas
# identicas registradas en blueprints distintos, Flask/Werkzeug le daba
# prioridad a esta version (registrada primero) -- que ni siquiera leia
# el body del POST. Resultado: los registros del modal de "Registrarse"
# probablemente nunca se estaban guardando. Ahora solo existe la
# version de auth.py.
