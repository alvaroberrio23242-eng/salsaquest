# app/models/timeline_data.py
"""
Modelos de Base de Datos para SalsaQuest (SQLAlchemy).
Estructura para los eventos y la línea de tiempo musical.
"""

from app import db


class TimelineData(db.Model):
    """Modelo para los nodos/eventos de la línea de tiempo."""
    __tablename__ = 'timeline_data'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(50), nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    trivia = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(255), nullable=True)
    audio_url = db.Column(db.String(255), nullable=True)  # 🎵 Muestra de audio/música

    def to_dict(self):
        """Convierte el objeto a diccionario para respuestas JSON."""
        return {
            "id": self.id,
            "anio": self.anio,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "trivia": self.trivia or "",
            "imagen": self.imagen or "https://via.placeholder.com/300x180?text=SalsaQuest",
            "audio_url": self.audio_url or ""
        }

    def __repr__(self):
        return f'<TimelineData {self.titulo}>'


# ALIAS DE COMPATIBILIDAD
Evento = TimelineData