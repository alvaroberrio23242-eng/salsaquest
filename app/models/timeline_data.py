# app/models/timeline_data.py

from app import db

class TimelineData(db.Model):
    __tablename__ = 'timeline_data'

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(20), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    imagen_url = db.Column(db.String(255), nullable=True)
    audio_url = db.Column(db.String(255), nullable=True)  # 👈 Campo para la canción/audio

    def to_dict(self):
        return {
            "id": self.id,
            "anio": self.anio,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "imagen_url": self.imagen_url,
            "audio_url": self.audio_url
        }