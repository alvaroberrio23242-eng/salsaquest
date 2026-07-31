"""
Inicialización de la aplicación Flask y configuración de extensiones/blueprints.
"""

import os
import secrets
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

    # SECRET_KEY: antes estaba hardcodeada en el codigo fuente (visible
    # para cualquiera que vea el repo), lo que compromete la seguridad
    # de las cookies de sesion del login de admin. Ahora se lee de la
    # variable de entorno SECRET_KEY (ponla en tu .env local y en las
    # variables de entorno de Render en produccion). Si no existe
    # ninguna (por ejemplo, la primera vez que corres en local sin
    # configurarla), se genera una aleatoria de forma automatica para
    # que la app no se rompa -- pero eso invalida las sesiones activas
    # cada vez que reinicies el servidor, asi que en produccion SIEMPRE
    # define SECRET_KEY explicitamente.
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'salsaquest.db')
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

    return app

# Alias para compatibilidad si alguna parte del proyecto busca 'create_app'
create_app = crear_app