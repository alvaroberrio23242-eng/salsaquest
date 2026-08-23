# app/routes/auth.py

from functools import wraps
import re
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from app.models.visit_counter import VisitCounter

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
    recordarme = bool(data.get('remember', False))

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'success': False, 'message': 'Usuario o contraseña incorrectos.'}), 401

    login_user(user, remember=recordarme)

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

# Validacion del POST publico del leaderboard. SQLite no aplica los
# VARCHAR(n) del modelo, asi que las longitudes se controlan aqui.
_EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
_PUNTAJE_MAX = 100000


def _validar_payload_leaderboard(data):
    """Retorna (campos_validos, None) o (None, mensaje_de_error_400)."""
    # La raiz del JSON debe ser un objeto; listas/strings/numeros se
    # rechazan con 400 en vez de romper con AttributeError.
    if not isinstance(data, dict):
        return None, 'El cuerpo debe ser un objeto JSON.'

    # P2: sin ningun campo con datos reales (ej. {}, solo
    # acepta_promociones o puntaje 0) se rechaza con 400 y no se crea
    # un lead anonimo con score 0.
    nombre_bruto = data.get('nombre_jugador') or data.get('username')
    puntaje_bruto = data.get('puntaje')
    hay_datos_reales = (
        (isinstance(nombre_bruto, str) and nombre_bruto.strip())
        or str(data.get('whatsapp') or '').strip()
        or str(data.get('email') or '').strip()
        or (isinstance(puntaje_bruto, int)
            and not isinstance(puntaje_bruto, bool)
            and puntaje_bruto > 0)
    )
    if not hay_datos_reales:
        return None, 'Debe enviar al menos un campo con datos.'

    nombre = data.get('nombre_jugador') or data.get('username') or 'Salsero Anónimo'
    if not isinstance(nombre, str):
        return None, 'El nombre debe ser texto.'
    nombre = nombre.strip()
    if len(nombre) > 100:
        return None, 'El nombre no puede superar 100 caracteres.'

    whatsapp = data.get('whatsapp', '')
    if not isinstance(whatsapp, str) or len(whatsapp) > 20:
        return None, 'WhatsApp inválido (máximo 20 caracteres).'

    email = data.get('email', '')
    if not isinstance(email, str) or len(email) > 120:
        return None, 'Email inválido (máximo 120 caracteres).'
    if email and not _EMAIL_RE.match(email):
        return None, 'Email inválido.'

    puntaje = data.get('puntaje', 0)
    if isinstance(puntaje, bool) or not isinstance(puntaje, int) \
            or not 0 <= puntaje <= _PUNTAJE_MAX:
        return None, 'Puntaje inválido (entero entre 0 y %d).' % _PUNTAJE_MAX

    acepta = data.get('acepta_promociones', True)
    if not isinstance(acepta, bool):
        return None, 'acepta_promociones debe ser booleano.'

    return {
        'nombre': nombre or 'Salsero Anónimo',
        'whatsapp': whatsapp,
        'email': email,
        'puntaje': puntaje,
        'acepta': acepta,
    }, None


@auth_bp.route('/api/leaderboard', methods=['POST'])
def registrar_usuario_o_puntaje():
    """Recibe los datos del modal de registro rápido / captura de WhatsApp."""
    data = request.get_json(silent=True)
    if data is None:
        if request.get_data():
            return jsonify({'error': 'Cuerpo JSON inválido.'}), 400
        data = {}

    campos, error = _validar_payload_leaderboard(data)
    if error:
        return jsonify({'error': error}), 400

    try:
        # 'username' es solo para cuentas con login tradicional
        # (register/login). Un lead del modal de leaderboard NO debe
        # setear username: como es unique=True, dos leads anonimos
        # (sin email, con nombre_jugador por defecto "Salsero Anonimo")
        # chocarian y el segundo se perderia con un error silencioso.
        nuevo_usuario = User(
            nombre_jugador=campos['nombre'],
            whatsapp=campos['whatsapp'],
            email=campos['email'] if campos['email'] else None,
            score=campos['puntaje'],
            acepta_promociones=campos['acepta']
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({
            'mensaje': '¡Usuario registrado correctamente!'
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@auth_bp.route('/api/leaderboard', methods=['GET'])
def obtener_leaderboard():
    """Retorna el Top 10 de mejores puntajes -- SIN datos de contacto,
    porque este endpoint es publico (cualquiera puede consultarlo)."""
    try:
        top_jugadores = User.query.order_by(User.score.desc()).limit(10).all()
        return jsonify([j.to_dict_public() for j in top_jugadores]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==========================================
# 3. PANEL DE ADMINISTRADOR (ver quien se registro)
# ==========================================

def admin_required(f):
    """Como @login_required, pero ademas exige is_admin=True."""
    @wraps(f)
    def decorada(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            return redirect(url_for('auth_bp.admin_login'))
        return f(*args, **kwargs)
    return decorada


@auth_bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Login del administrador, con casilla 'recordarme' para no tener
    que iniciar sesion de nuevo cada vez (cookie persistente 30 dias)."""
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('auth_bp.admin_panel'))

    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        recordarme = request.form.get('remember') == 'on'

        user = User.query.filter_by(username=username).first()

        if user and user.is_admin and user.check_password(password):
            login_user(user, remember=recordarme)
            return redirect(url_for('auth_bp.admin_panel'))

        error = 'Usuario o contraseña incorrectos, o esta cuenta no tiene acceso de administrador.'

    return render_template('admin_login.html', error=error)


@auth_bp.route('/admin')
@admin_required
def admin_panel():
    """Panel con la lista de todos los que dejaron sus datos
    (nombre, email, whatsapp, puntaje, fecha) y el contador de visitas."""
    usuarios = User.query.order_by(User.fecha_registro.desc()).all()
    fila_visitas = VisitCounter.query.first()
    total_visitas = fila_visitas.total if fila_visitas else 0
    return render_template(
        'admin_panel.html',
        usuarios=usuarios,
        total_visitas=total_visitas,
        admin=current_user,
    )


@auth_bp.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('auth_bp.admin_login'))
