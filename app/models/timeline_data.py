# app/models/timeline_data.py
"""
Modelos de Base de Datos para SalsaQuest (SQLAlchemy).
Contiene la estructura para la línea de tiempo y la puntuación de los usuarios.
"""

from app import db


class Evento(db.Model):
    """Modelo para los nodos/eventos de la línea de tiempo."""
    __tablename__ = 'eventos'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    era = db.Column(db.String(50), nullable=True, default='raices')
    anio = db.Column(db.Integer, nullable=False)
    anio_fin = db.Column(db.Integer, nullable=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    dato_curioso = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(255), nullable=True)
    audio_url = db.Column(db.String(255), nullable=True)  # 🎵 Campo de audio / música

    def to_dict(self):
        """Convierte el objeto a diccionario para respuestas JSON de las APIs."""
        return {
            "id": self.id,
            "era": self.era or "raices",
            "anio": self.anio,
            "anio_inicio": self.anio,
            "anio_fin": self.anio_fin,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "descripcion_corta": self.descripcion,
            "dato_curioso": self.dato_curioso,
            "imagen_url": self.imagen_url or "https://via.placeholder.com/300x180?text=SalsaQuest",
            "audio_url": self.audio_url or ""
        }


class UsuarioProgreso(db.Model):
    """Modelo para guardar la puntuación y avance de los jugadores."""
    __tablename__ = 'usuario_progreso'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nombre_jugador = db.Column(db.String(80), nullable=False)
    puntaje = db.Column(db.Integer, default=0)
    nivel_alcanzado = db.Column(db.Integer, default=1)

    def to_dict(self):
        """Convierte el progreso del usuario a diccionario JSON."""
        return {
            "id": self.id,
            "nombre_jugador": self.nombre_jugador,
            "puntaje": self.puntaje,
            "nivel_alcanzado": self.nivel_alcanzado
        }