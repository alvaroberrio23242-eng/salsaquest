"""
Inicialización de la aplicación Flask y configuración de extensiones/blueprints.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Instancia global de SQLAlchemy
db = SQLAlchemy()

# Instancia global de Flask-Login. Se inicializa (init_app) dentro de
# crear_app(), pero se define aqui arriba para poder importarla desde
# otros modulos si hiciera falta.
login_manager = LoginManager()


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

    # --- Flask-Login ---
    # Sin esto, login_user()/current_user/@login_required no funcionan:
    # no hay nada que guarde ni recupere la sesion del usuario logueado.
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