"""
Punto de entrada de la aplicación SalsaQuest.
Inicializa la base de datos y levanta el servidor Flask / WSGI.
"""

from app import crear_app, db

# Crear la instancia de la aplicación Flask
app = crear_app()

if __name__ == '__main__':
    # Asegurar que las tablas de la base de datos existan al ejecutar localmente
    with app.app_context():
        db.create_all()
    
    # Ejecutar servidor de desarrollo
    app.run(debug=True)