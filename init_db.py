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
from app.models.timeline_data import TimelineData

app = crear_app()

eventos_salsa = [
    {
        "anio": "1900-1940",
        "titulo": "Son Cubano",
        "descripcion": "Fusión de ritmos africanos y españoles en Cuba que sentó las bases de la salsa.",
        "trivia": "El son nació en las zonas rurales del oriente cubano antes de tomar La Habana.",
        "imagen_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/5A1L6S0GIs4"
    },
    {
        "anio": "1964",
        "titulo": "Nacimiento de Fania Records",
        "descripcion": "Jerry Masucci y Johnny Pacheco fundan el sello clave en la masificación de la salsa.",
        "trivia": "Pacheco vendía los primeros discos de Fania directamente en el baúl de su auto.",
        "imagen_url": "https://images.unsplash.com/photo-1539375665275-f9de415ef9ac?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/409C1vLvh-8"
    },
    {
        "anio": "1967",
        "titulo": "Debut de Willie Colón y Héctor Lavoe",
        "descripcion": "Lanzan el álbum 'El Malo', iniciando una de las duplas más icónicas del género.",
        "trivia": "Willie tenía solo 17 años cuando grabó este emblemático disco.",
        "imagen_url": "https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/j_8K3XU_0iI"
    },
    {
        "anio": "1974",
        "titulo": "Celia Cruz & Fania en África",
        "descripcion": "Histórico concierto en Zaire junto a la mítica pelea de boxeo entre Ali y Foreman.",
        "trivia": "Celia Cruz deslumbró al público africano gritando por primera vez con fuerza '¡Azúcar!'",
        "imagen_url": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/S2p0Pz9aHms"
    },
    {
        "anio": "1978",
        "titulo": "Lanzamiento de 'Siembra'",
        "descripcion": "Willie Colón y Rubén Blades lanzan el álbum de salsa más vendido de la historia.",
        "trivia": "Incluye 'Pedro Navaja', un tema que los ejecutivos del sello no querían incluir por ser muy largo.",
        "imagen_url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/JmGvK5mR3kE"
    },
    {
        "anio": "1981",
        "titulo": "Grupo Niche & Jairo Varela",
        "descripcion": "Jairo Varela consolida al Grupo Niche en Colombia, convirtiendo a Cali en la Capital de la Salsa.",
        "trivia": "Jairo Varela compuso clásicos eternos sin tocar instrumentos armónicos, tarareando sus arreglos.",
        "imagen_url": "https://images.unsplash.com/photo-1539375665275-f9de415ef9ac?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/L1d4gU0mF-A"
    },
    {
        "anio": "1995",
        "titulo": "La Timba Cubana: Los Van Van",
        "descripcion": "Juan Formell y Los Van Van revolucionan Cuba y el mundo con la explosión de la Timba.",
        "trivia": "Juan Formell creó el ritmo 'Songo' y fusionó sintetizadores con la charanga tradicional.",
        "imagen_url": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=500",
        "audio_url": "https://www.youtube-nocookie.com/embed/rP3v6q_S8f8"
    }
]


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

        # --- Eventos de la timeline: solo se siembran si la tabla esta vacia ---
        if TimelineData.query.count() == 0:
            for data in eventos_salsa:
                evento = TimelineData(
                    anio=data['anio'],
                    titulo=data['titulo'],
                    descripcion=data['descripcion'],
                    trivia=data.get('trivia'),
                    imagen_url=data['imagen_url'],
                    audio_url=data['audio_url']
                )
                db.session.add(evento)
            print("Eventos historicos de la timeline cargados.")
        else:
            print("La timeline ya tenia datos, no se volvio a sembrar.")

        db.session.commit()
        print("¡Base de datos lista! (usuarios y puntajes existentes se conservaron) 🎬💃")


if __name__ == '__main__':
    poblar_base_datos()
