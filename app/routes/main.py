# app/routes/main.py
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('inicio.html', active_page='inicio')


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


@main_bp.route('/son-havana')
def son_havana():
    return render_template('son_havana.html', active_page='son_havana')


@main_bp.route('/grammy')
def grammy():
    return render_template('grammy.html', active_page='grammy')


@main_bp.route('/timba')
def timba():
    return render_template('timba.html', active_page='timba')


@main_bp.route('/trivia')
def trivia_page():
    return render_template('trivia.html', active_page='trivia')


@main_bp.route('/recursos')
def recursos():
    return render_template('recursos.html', active_page='recursos')


# NOTA: la ruta /api/leaderboard (GET y POST) se quito de aqui. Vivia
# duplicada tambien en app/routes/auth.py con distinta logica (esa si
# guarda el registro/lead en la base de datos), y al haber dos rutas
# identicas registradas en blueprints distintos, Flask/Werkzeug le daba
# prioridad a esta version (registrada primero) -- que ni siquiera leia
# el body del POST. Resultado: los registros del modal de "Registrarse"
# probablemente nunca se estaban guardando. Ahora solo existe la
# version de auth.py.
