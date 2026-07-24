# app/models/timeline_data.py
"""
Modelo de datos para la línea de tiempo histórica de SalsaQuest.
"""

from app import db


class TimelineData(db.Model):
    __tablename__ = 'timeline_data'

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(10), nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    trivia = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(255), nullable=True)
    audio_url = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convierte la instancia del modelo a un diccionario serializable en JSON."""
        return {
            'id': self.id,
            'anio': self.anio,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'trivia': self.trivia,
            'imagen_url': self.imagen_url,
            'audio_url': self.audio_url
        }