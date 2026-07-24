# app/__init__.py

"""
Application factory de SalsaQuest.
Aquí se crea la instancia de Flask y se registran los Blueprints (rutas).
"""

from flask import Flask


def crear_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    from app.routes.timeline import timeline_bp
    app.register_blueprint(timeline_bp)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app