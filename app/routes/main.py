# app/routes/main.py

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Sirve la página principal con la línea de tiempo."""
    return render_template('index.html')
