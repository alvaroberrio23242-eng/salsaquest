"""
Modelo de la línea de tiempo de SalsaQuest.

IMPORTANTE: este archivo antes NO tenia ninguna clase de modelo -- en
algun momento se reemplazo por completo con una lista de datos de
prueba (en ingles: "year", "title", "image_url"...) llamada tambien
"TimelineData", que tapaba el nombre de la clase real. Como el resto
del codigo (routes/timeline.py, init_db.py) importa "TimelineData"
esperando la clase de SQLAlchemy (con .query, .to_dict(), etc.), esto
rompia todo con "AttributeError: 'list' object has no attribute
'query'". Aqui esta la clase reconstruida con los campos que el resto
del proyecto realmente usa.
"""

from app import db


class TimelineData(db.Model):
    __tablename__ = "timeline_data"

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(20), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    trivia = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(500), nullable=True)
    audio_url = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        """Convierte la fila a un diccionario serializable a JSON,
        con las claves en español que espera el frontend
        (timeline.js / content.js)."""
        return {
            "id": self.id,
            "anio": self.anio,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "trivia": self.trivia,
            "imagen_url": self.imagen_url,
            "audio_url": self.audio_url,
        }

    def __repr__(self):
        return f"<TimelineData {self.anio} - {self.titulo}>"