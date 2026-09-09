# init_db.py
"""
Script para inicializar y poblar la base de datos de SalsaQuest.
Crea la estructura de tablas, registra un administrador SOLO si ADMIN_USERNAME/ADMIN_PASSWORD están en el entorno, y carga los eventos históricos de salsa.

IMPORTANTE: este script ahora es IDEMPOTENTE -- se puede correr las
veces que sea (por ejemplo, en cada despliegue en Render) sin borrar
usuarios, puntajes ni datos ya existentes. Antes hacia db.drop_all()
que arrasaba con TODO en cada ejecucion; eso era peligroso si alguna
vez se llamaba a este script en produccion, o si build.sh volvia a
incluir "python init_db.py" por error.
"""

import os
from app import crear_app, db
from app.models.user import User
from app.routes.timeline import sembrar_eventos_faltantes

app = crear_app()


def poblar_base_datos():
    with app.app_context():
        db.create_all()

        # --- Usuario administrador: solo con credenciales del entorno.
        # Sin ADMIN_USERNAME/ADMIN_PASSWORD no se crea ningun admin;
        # los administradores existentes nunca se modifican aqui.
        admin_username = os.environ.get('ADMIN_USERNAME')
        admin_password = os.environ.get('ADMIN_PASSWORD')
        if admin_username and admin_password:
            admin_existente = User.query.filter_by(username=admin_username).first()
            if not admin_existente:
                admin = User(
                    username=admin_username,
                    email=os.environ.get('ADMIN_EMAIL'),
                    score=200,
                    is_admin=True,
                )
                admin.set_password(admin_password)
                db.session.add(admin)
                print("Usuario administrador creado desde variables de entorno.")
            else:
                print("El usuario administrador ya existia, no se modifico.")
        else:
            print("ADMIN_USERNAME/ADMIN_PASSWORD no configuradas: no se crea ningun administrador.")

        # --- Eventos de la timeline: siembra canonica compartida con
        # /api/timeline (misma fuente unica, misma logica idempotente) ---
        sembrar_eventos_faltantes()
        print("Eventos historicos de la timeline verificados/actualizados.")

        db.session.commit()
        print("¡Base de datos lista! (usuarios y puntajes existentes se conservaron) 🎬💃")


if __name__ == '__main__':
    poblar_base_datos()
