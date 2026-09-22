import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuración de Clave Secreta
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_por_defecto')

    # Configuración dinámica de la Base de Datos
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        # Render a veces entrega URLs con 'postgres://', SQLAlchemy requiere 'postgresql://'
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    else:
        # Fallback a SQLite para desarrollo local en tu equipo
        base_dir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'sonhavana.db')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Registro de Blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
