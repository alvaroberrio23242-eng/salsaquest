"""
Punto de entrada de la aplicación SalsaQuest.
Inicializa la base de datos y levanta el servidor Flask / WSGI.
"""

from app import crear_app, db

app = crear_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)