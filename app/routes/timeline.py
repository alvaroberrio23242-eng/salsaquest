from flask import Blueprint, jsonify
from app.models.timeline_data import TimelineData
from app import db

timeline_bp = Blueprint('timeline', __name__)

@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()
        
        # Si la base de datos en Render está vacía, insertamos los datos iniciales automáticamente
        if not eventos:
            datos_iniciales = [
                TimelineData(
                    anio="1950",
                    titulo="Raíces del Son Cubano y Mambo",
                    descripcion="El son cubano, la guaracha y el mambo se expanden por el Caribe y Nueva York, sentando las bases rítmicas de lo que más adelante se llamaría Salsa.",
                    trivia="¿Qué ritmo popularizado por Pérez Prado en los 50 influyó en la salsa?",
                    imagen_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500",
                    audio_url="https://www.youtube.com/embed/z59gA2RMO10"
                ),
                TimelineData(
                    anio="1964",
                    titulo="Fundación de Fania Records",
                    descripcion="Jerry Masucci y Johnny Pacheco fundan Fania Records en Nueva York, sello discográfico clave en la masificación mundial de la salsa.",
                    trivia="¿Quién fue el flautista y cofundador de Fania Records junto a Jerry Masucci?",
                    imagen_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=500",
                    audio_url="https://www.youtube.com/embed/ypNIs_9K7xY"
                ),
                TimelineData(
                    anio="1971",
                    titulo="Concierto en el Cheetah Club",
                    descripcion="La Fania All-Stars se presenta en el Cheetah Club de Nueva York. El concierto fue grabado para la histórica película 'Our Latin Thing'.",
                    trivia="¿Cómo se llamó el famoso documental grabado en el Cheetah Club en 1971?",
                    imagen_url="https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=500",
                    audio_url="https://www.youtube.com/embed/3O2f2CkW8eE"
                ),
                TimelineData(
                    anio="1980",
                    titulo="Llegada de la Salsa Romántica",
                    descripcion="Nace una nueva corriente liderada por artistas como Frankie Ruiz, Eddie Santiago y Lalo Rodríguez, centrada en letras sobre el amor y el desamor.",
                    trivia="¿Quién es conocido mundialmente como 'El Papá de la Salsa'?",
                    imagen_url="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=500",
                    audio_url="https://www.youtube.com/embed/mKk3m0M3JbE"
                )
            ]
            
            for ev in datos_iniciales:
                db.session.add(ev)
            db.session.commit()
            
            eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()

        return jsonify([e.to_dict() for e in eventos])

    except Exception as e:
        print(f"Error en /api/timeline: {e}")
        return jsonify({"error": str(e)}), 500