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

import pytest
from app import crear_app, db as _db


@pytest.fixture(scope="session")
def app():
    """Crea la instancia Flask una vez por sesión de pruebas."""
    app = crear_app()
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
