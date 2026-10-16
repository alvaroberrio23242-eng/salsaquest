# tests/conftest.py
"""Fixtures compartidas para pytest — SalsaQuest."""

import os
import sys
from pathlib import Path

# Asegurar que el root del proyecto esté en sys.path para que
# `from app import crear_app` funcione desde cualquier directorio.
_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

# Cargar .variables de entorno antes de importar la app
from dotenv import load_dotenv
load_dotenv(Path(_root) / ".env")

# Fase A: los tests NUNCA tocan la BD local (sonhavana.db).
# Se fija ANTES de crear_app(), porque Flask-SQLAlchemy 3.x crea los engines
# dentro de db.init_app() y los cambios posteriores en app.config no se
# reflejan (docstring de init_app). Así la app nace ya con la URI en memoria
# y create_all()/drop_all() solo operan sobre ella.
TEST_DB_URI = "sqlite:///:memory:"
os.environ["DATABASE_URL"] = TEST_DB_URI

import pytest
from app import crear_app, db as _db


@pytest.fixture(scope="session")
def app():
    """Crea la instancia Flask una vez por sesión de pruebas."""
    app = crear_app()
    # Guarda: si la app no nació en memoria, fallar antes de tocar cualquier BD.
    assert app.config["SQLALCHEMY_DATABASE_URI"] == TEST_DB_URI, (
        "Los tests deben usar SQLite en memoria, nunca la BD local"
    )
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    """Cliente de pruebas HTTP."""
    return app.test_client()
