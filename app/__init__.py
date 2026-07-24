# app/__init__.py
"""
Inicialización de la aplicación Flask y configuración de extensiones/blueprints.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia de SQLAlchemy
db = SQLAlchemy()

def crear_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    # Configuración de la base de datos SQLite
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SECRET_KEY'] = 'salsa_quest_secret_key_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'sonhavana.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la app
    db.init_app(app)

    # Registrar los Blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.timeline import timeline_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(timeline_bp)

    return app