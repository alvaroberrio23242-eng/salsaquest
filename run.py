# run.py

"""
Punto de entrada de la aplicación.
Este es el archivo que se ejecuta para levantar el servidor de desarrollo.
"""

from app import crear_app

app = crear_app()

if __name__ == '__main__':
    app.run(debug=True)