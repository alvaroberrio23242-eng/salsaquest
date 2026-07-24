# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def crear_app():
    app = Flask(__name__)

    # Configuración de la Base de Datos SQLite
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, '..', 'salsaquest.db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    db.init_app(app)

    # Registrar Blueprints
    from app.routes.timeline import timeline_bp
    app.register_blueprint(timeline_bp)

    return app