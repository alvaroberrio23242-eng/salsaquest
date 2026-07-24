from flask import Blueprint, jsonify
from app.models.timeline_data import TimelineData
from app import db

timeline_bp = Blueprint('timeline', __name__)

@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()
        
        # Si la base de datos está vacía o si queremos resetear los eventos predeterminados
        if not eventos:
            datos_iniciales = [
                TimelineData(
                    anio="1950",
                    titulo="Raíces del Son Cubano y Mambo",
                    descripcion="El son cubano, la guaracha y el mambo se expanden por el Caribe y Nueva York, sentando las bases rítmicas de la Salsa.",
                    trivia="¿Sabías que Dámaso Pérez Prado popularizó el Mambo en México antes de llevarlo a nivel mundial?",
                    imagen_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500",
                    audio_url="https://www.youtube.com/embed/zxC3y2AAnls" # Mambo No. 5 - Perez Prado
                ),
                TimelineData(
                    anio="1964",
                    titulo="Fundación de Fania Records",
                    descripcion="Jerry Masucci y Johnny Pacheco fundan Fania Records en Nueva York, el sello discográfico clave en la historia de la salsa.",
                    trivia="Johnny Pacheco repartía los primeros discos de Fania en el maletero de su propio auto.",
                    imagen_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=500",
                    audio_url="https://www.youtube.com/embed/5a4G3R8U6L0" # Fania All Stars Documental Clip
                ),
                TimelineData(
                    anio="1971",
                    titulo="Concierto Histórico en el Cheetah Club",
                    descripcion="La Fania All-Stars se presenta en el Cheetah Club de Nueva York, inmortalizado en el famoso documental 'Our Latin Thing'.",
                    trivia="Esa noche reunió a figuras estelares como Héctor Lavoe, Cheo Feliciano, Ismael Miranda y Ray Barretto.",
                    imagen_url="https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=500",
                    audio_url="https://www.youtube.com/embed/aE1qC5sU-M0" # Anacaona - Cheo Feliciano / Fania
                ),
                TimelineData(
                    anio="1978",
                    titulo="Lanzamiento del Álbum 'Siembra'",
                    descripcion="Willie Colón y Rubén Blades lanzan 'Siembra', convirtiéndose en el álbum más vendido en la historia de la salsa.",
                    trivia="Contiene clásicos épicos de la salsa con conciencia social como 'Pedro Navaja' y 'Plástico'.",
                    imagen_url="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=500",
                    audio_url="https://www.youtube.com/embed/hJipO43MByM" # Pedro Navaja
                )
            ]
            for ev in datos_iniciales:
                db.session.add(ev)
            db.session.commit()
            eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()

        return jsonify([e.to_dict() for e in eventos])
    except Exception as e:
        return jsonify({"error": str(e)}), 500