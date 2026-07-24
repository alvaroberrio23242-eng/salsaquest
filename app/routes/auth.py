# app/routes/auth.py

from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User

# Definición unificada del Blueprint
auth_bp = Blueprint('auth_bp', __name__)

# ==========================================
# 1. AUTENTICACIÓN TRADICIONAL (Login/Register)
# ==========================================

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json() or request.form

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'success': False, 'message': 'Faltan datos requeridos.'}), 400

    # Verificar existencia previa
    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'message': 'El nombre de usuario ya está registrado.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'El correo electrónico ya está registrado.'}), 400

    # Crear usuario completo
    nuevo_usuario = User(
        username=username, 
        nombre_jugador=username, 
        email=email
    )
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    login_user(nuevo_usuario)

    return jsonify({
        'success': True,
        'message': f'¡Bienvenido a SalsaQuest, {username}!',
        'user': {'username': username, 'score': nuevo_usuario.score}
    }), 201


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json() or request.form

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'success': False, 'message': 'Usuario o contraseña incorrectos.'}), 401

    login_user(user)

    return jsonify({
        'success': True,
        'message': f'¡Hola de nuevo, {user.username}!',
        'user': {'username': user.username, 'score': user.score}
    }), 200


@auth_bp.route('/auth/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'success': True, 'message': 'Sesión cerrada correctamente.'})


@auth_bp.route('/auth/current_user', methods=['GET'])
def get_current_user():
    """Retorna los datos del usuario autenticado actualmente."""
    if current_user.is_authenticated:
        return jsonify({
            'authenticated': True,
            'username': current_user.username or current_user.nombre_jugador,
            'score': current_user.score
        })
    return jsonify({'authenticated': False})


# ==========================================
# 2. CAPTURA DE LEADS Y LEADERBOARD (Ranking)
# ==========================================

@auth_bp.route('/api/leaderboard', methods=['POST'])
def registrar_usuario_o_puntaje():
    """Recibe los datos del modal de registro rápido / captura de WhatsApp."""
    data = request.get_json() or {}

    nombre = data.get('nombre_jugador') or data.get('username') or 'Salsero Anónimo'
    whatsapp = data.get('whatsapp', '')
    email = data.get('email', '')
    puntaje = data.get('puntaje', 0)
    acepta = data.get('acepta_promociones', True)

    try:
        nuevo_usuario = User(
            nombre_jugador=nombre,
            username=nombre if not email else None,
            whatsapp=whatsapp,
            email=email if email else None,
            score=puntaje,
            acepta_promociones=acepta
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({
            'mensaje': '¡Usuario registrado correctamente!',
            'cupon': 'SONHAVANA10OFF'
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@auth_bp.route('/api/leaderboard', methods=['GET'])
def obtener_leaderboard():
    """Retorna el Top 10 de mejores puntajes."""
    try:
        top_jugadores = User.query.order_by(User.score.desc()).limit(10).all()
        return jsonify([j.to_dict() for j in top_jugadores]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500