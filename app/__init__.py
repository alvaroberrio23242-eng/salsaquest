import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializamos el objeto SQLAlchemy fuera de crear_app
db = SQLAlchemy()

def crear_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    # Configuración de SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sonhavana.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    # Conectar la base de datos con la app
    db.init_app(app)

    # Registrar los Blueprints
    from app.routes.timeline import timeline_bp
    from app.routes.main import main_bp

    app.register_blueprint(timeline_bp)
    app.register_blueprint(main_bp)

    return app