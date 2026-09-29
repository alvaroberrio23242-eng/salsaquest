"""
Inicialización de la aplicación Flask y configuración de extensiones/blueprints.
"""

import os
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Instancia global de SQLAlchemy
db = SQLAlchemy()
login_manager = LoginManager()

def crear_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    # Configuración básica y de la clave secreta
    base_dir = os.path.abspath(os.path.dirname(__file__))
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY no esta configurada. Definela como variable de "
            "entorno antes de arrancar la aplicacion."
        )
    app.config['SECRET_KEY'] = secret_key

    # Configuración dinámica de la Base de Datos (PostgreSQL en Render / SQLite local)
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'sonhavana.db')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # "Recordar acceso": cuánto dura la cookie de sesión persistente
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.admin_login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.query.get(int(user_id))

    # Importar y registrar todos los Blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.timeline import timeline_bp
    from app.routes.content import content_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(timeline_bp)
    app.register_blueprint(content_bp)

    # Crear tablas en la base de datos si no existen al arrancar
    with app.app_context():
        from app.models.timeline_data import TimelineData
        from app.models.user import User
        from app.models.visit_counter import VisitCounter
        db.create_all()

    # --- Cache-Control headers ---
    @app.after_request
    def set_cache_headers(response):
        from flask import request
        if request.path.startswith('/static/'):
            response.headers['Cache-Control'] = 'public, max-age=3600'
        else:
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
        return response

    return app

# Alias para compatibilidad si alguna parte del proyecto busca 'create_app'
create_app = crear_app
