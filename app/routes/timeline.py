from flask import Blueprint, jsonify
from app.models.timeline_data import TimelineData
from app import db

timeline_bp = Blueprint('timeline', __name__)

# Datos semilla: se insertan UNA sola vez (solo si la tabla esta vacia).
# Antes, este endpoint borraba y volvia a insertar estos 4 eventos en
# CADA visita a la pagina (db.session.query(TimelineData).delete()),
# lo que ademas se disparaba DOS VECES por carga de pagina (timeline.js
# Y content.js pedian /api/timeline por separado) -- en SQLite esto
# podia chocar como "database is locked" y mostrar "Error al cargar".
_EVENTOS_SEMILLA = [
    dict(
        anio="1950",
        titulo="Raices del Son Cubano y Mambo",
        descripcion="El son cubano, la guaracha y el mambo se expanden por el Caribe y Nueva York, sentando las bases ritmicas de la Salsa.",
        trivia="Sabias que Damaso Perez Prado popularizo el Mambo en Mexico antes de llevarlo a nivel mundial?",
        imagen_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500",
        audio_url="https://www.youtube.com/embed/zxC3y2AAnls",
    ),
    dict(
        anio="1964",
        titulo="Fundacion de Fania Records",
        descripcion="Jerry Masucci y Johnny Pacheco fundan Fania Records en Nueva York, el sello discografico clave en la historia de la salsa.",
        trivia="Johnny Pacheco repartia los primeros discos de Fania en el maletero de su propio auto.",
        imagen_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=500",
        audio_url="https://www.youtube.com/embed/5a4G3R8U6L0",
    ),
    dict(
        anio="1971",
        titulo="Concierto Historico en el Cheetah Club",
        descripcion="La Fania All-Stars se presenta en el Cheetah Club de Nueva York, inmortalizado en el famoso documental 'Our Latin Thing'.",
        trivia="Esa noche reunio a figuras estelares como Hector Lavoe, Cheo Feliciano, Ismael Miranda y Ray Barretto.",
        imagen_url="https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=500",
        audio_url="https://www.youtube.com/embed/aE1qC5sU-M0",
    ),
    dict(
        anio="1978",
        titulo="Lanzamiento del Album 'Siembra'",
        descripcion="Willie Colon y Ruben Blades lanzan 'Siembra', convirtiendose en el album mas vendido en la historia de la salsa.",
        trivia="Contiene clasicos epicos de la salsa con conciencia social como 'Pedro Navaja' y 'Plastico'.",
        imagen_url="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=500",
        audio_url="https://www.youtube.com/embed/hJipO43MByM",
    ),
]


@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        # Solo siembra los datos si la tabla esta realmente vacia (primera
        # vez que corre la app). Ya NO borra nada en cada peticion.
        if TimelineData.query.count() == 0:
            for datos in _EVENTOS_SEMILLA:
                db.session.add(TimelineData(**datos))
            db.session.commit()

        eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()
        return jsonify([e.to_dict() for e in eventos])

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
