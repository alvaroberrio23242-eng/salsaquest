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

    # Configuración básica y de la base de datos SQLite
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # La clave de sesiones NUNCA se hardcodea: sin SECRET_KEY en el
    # entorno la app se niega a arrancar (fail-fast).
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY no esta configurada. Definela como variable de "
            "entorno antes de arrancar la aplicacion."
        )
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'sonhavana.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # "Recordar acceso": cuanto dura la cookie de sesion persistente
    # cuando el login se hace con remember=True (ver auth.py)
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
        # Importar los modelos para que SQLAlchemy reconozca la estructura
        from app.models.timeline_data import TimelineData 
        from app.models.user import User
        from app.models.visit_counter import VisitCounter
        db.create_all()

    # --- Cache-Control headers ---
    # HTML: no-cache para que el navegador siempre pida la version
    # mas reciente al servidor (evita contenido desactualizado en
    # Render o cualquier CDN/browser cache).
    @app.after_request
    def set_cache_headers(response):
        from flask import request
        if request.path.startswith('/static/'):
            # Assets estaticos: permitir cache 1 hora (gunicorn sirve
            # directamente desde disco, no hay CDN intermedio en Render
            # free tier). Si se agrega CDN en el futuro, subir este TTL.
            response.headers['Cache-Control'] = 'public, max-age=3600'
        else:
            # HTML y APIs: nunca cachear
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
        return response

    return app

# Alias para compatibilidad si alguna parte del proyecto busca 'create_app'
create_app = crear_app