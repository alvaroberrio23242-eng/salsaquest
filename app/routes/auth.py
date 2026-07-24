# app/routes/auth.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or request.form

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'success': False, 'message': 'Faltan datos requeridos.'}), 400

    # Verificar si el usuario o email ya existen
    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'message': 'El nombre de usuario ya está registrado.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'El correo electrónico ya está registrado.'}), 400

    # Crear nuevo usuario
    nuevo_usuario = User(username=username, email=email)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    # Iniciar sesión automáticamente
    login_user(nuevo_usuario)

    return jsonify({
        'success': True,
        'message': f'¡Bienvenido a SalsaQuest, {username}!',
        'user': {'username': username, 'score': nuevo_usuario.score}
    })


@auth_bp.route('/login', methods=['POST'])
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
    })


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'success': True, 'message': 'Sesión cerrada correctamente.'})


@auth_bp.route('/current_user', methods=['GET'])
def get_current_user():
    """Retorna los datos del usuario autenticado actualmente."""
    if current_user.is_authenticated:
        return jsonify({
            'authenticated': True,
            'username': current_user.username,
            'score': current_user.score
        })
    return jsonify({'authenticated': False})