from app import crear_app, db
from app.models.timeline_data import Evento, UsuarioProgreso

app = crear_app()

with app.app_context():
    # 1. Eliminar y recrear todas las tablas
    db.drop_all()
    db.create_all()
    print("¡Base de datos limpia y tablas reestructuradas!")

    # 2. Insertar eventos iniciales de prueba con imágenes
    eventos_iniciales = [
        Evento(
            era="raices",
            anio=1900,
            anio_fin=1940,
            titulo="Son Cubano",
            descripcion="Fusión de ritmos africanos y españoles en Cuba que sentó las bases del género.",
            dato_curioso="El Son se popularizó en La Habana a través de las agrupaciones de sextetos y septetos.",
            imagen_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500"
        ),
        Evento(
            era="nueva_york",
            anio=1964,
            titulo="Nacimiento de Fania Records",
            descripcion="Jerry Masucci y Johnny Pacheco fundan el sello clave en la masificación de la salsa.",
            dato_curioso="Comenzaron vendiendo discos directamente desde el maletero de un coche en Nueva York.",
            imagen_url="https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=500"
        ),
        Evento(
            era="fania",
            anio=1971,
            titulo="Concierto en El Cheetah",
            descripcion="Las Estrellas de Fania ofrecen un histórico concierto grabado en vivo.",
            dato_curioso="De este concierto nació la película documental 'Our Latin Thing'.",
            imagen_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=500"
        ),
        Evento(
            era="expansion",
            anio=1978,
            titulo="Lanzamiento de 'Siembra'",
            descripcion="Willie Colón y Rubén Blades lanzan uno de los álbumes más vendidos del género.",
            dato_curioso="El tema 'Pedro Navaja' dura más de 7 minutos, rompiendo el estándar comercial de radio.",
            imagen_url="https://images.unsplash.com/photo-1511735111819-9a3f7709049c?w=500"
        )
    ]

    # 3. Insertar un jugador inicial en el Leaderboard
    jugador_demo = UsuarioProgreso(
        nombre_jugador="Hector Lavoe",
        puntaje=50,
        nivel_alcanzado=2
    )

    db.session.add_all(eventos_iniciales)
    db.session.add(jugador_demo)
    db.session.commit()

    print("¡Datos de prueba insertados con éxito! 🎶")
    # init_db.py
from app import crear_app, db
from app.models.timeline_data import Evento, UsuarioProgreso

app = crear_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("¡Base de datos y tablas reconstruidas!")

    eventos_iniciales = [
        Evento(
            era="raices",
            anio=1900,
            anio_fin=1940,
            titulo="Son Cubano",
            descripcion="Fusión de ritmos africanos y españoles en Cuba que sentó las bases del género.",
            dato_curioso="El Son se popularizó en La Habana a través de las agrupaciones de sextetos y septetos.",
            imagen_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"  # 🎵 MP3 de prueba
        ),
        Evento(
            era="nueva_york",
            anio=1964,
            titulo="Nacimiento de Fania Records",
            descripcion="Jerry Masucci y Johnny Pacheco fundan el sello clave en la masificación de la salsa.",
            dato_curioso="Comenzaron vendiendo discos directamente desde el maletero de un coche en Nueva York.",
            imagen_url="https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=500",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        ),
        Evento(
            era="fania",
            anio=1971,
            titulo="Concierto en El Cheetah",
            descripcion="Las Estrellas de Fania ofrecen un histórico concierto grabado en vivo.",
            dato_curioso="De este concierto nació la película documental 'Our Latin Thing'.",
            imagen_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=500",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        )
    ]

    jugador_demo = UsuarioProgreso(
        nombre_jugador="Hector Lavoe",
        puntaje=50,
        nivel_alcanzado=2
    )

    db.session.add_all(eventos_iniciales)
    db.session.add(jugador_demo)
    db.session.commit()

    print("¡Base de datos lista con audios e imágenes de prueba! 🎶")