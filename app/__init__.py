"""
Inicialización de la aplicación Flask y configuración de extensiones/blueprints.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia global de SQLAlchemy
db = SQLAlchemy()

def crear_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    # Configuración básica y de la base de datos SQLite
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SECRET_KEY'] = 'salsa_quest_secret_key_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'sonhavana.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la extensión de base de datos
    db.init_app(app)

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