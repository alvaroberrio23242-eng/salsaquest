# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializar las extensiones fuera de la fábrica de la app
db = SQLAlchemy()
login_manager = LoginManager()

def crear_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)
    
    # Clave secreta necesaria para manejar sesiones e inicios de sesión
    app.config['SECRET_KEY'] = 'salsaquest_secret_key_2026'

    # Configuración de la base de datos SQLite
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, '..', 'sonhavana.db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    # Conectar las extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'  # Redirección si el usuario no ha iniciado sesión

    # Cargar el usuario actual de la sesión
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar todos los Blueprints (Rutas)
    from app.routes.timeline import timeline_bp
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(timeline_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app