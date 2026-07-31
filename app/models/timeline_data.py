# app/models/timeline_data.py
"""
Modelo de la linea de tiempo de la historia de la salsa.

IMPORTANTE: este archivo tuvo una regresion mas de una vez -- se
reemplazo por una simple lista de Python con nombres de campo en
ingles (year/title/description/...), lo cual rompe tanto init_db.py
como app/routes/timeline.py (ambos esperan un modelo SQLAlchemy real
con estos nombres de columna en espanol: anio/titulo/descripcion/
trivia/imagen_url/audio_url). Restaurado aqui -- si vuelve a
"romperse" el timeline, revisa primero que este archivo siga siendo
una clase db.Model y no una lista.
"""

from app import db


class TimelineData(db.Model):
    __tablename__ = 'timeline_data'

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(20), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    artista = db.Column(db.String(200), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    trivia = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(500), nullable=True)
    audio_url = db.Column(db.String(500), nullable=True)
    # ID de album de Spotify para mostrar la caratula real via embed
    # oficial (mismo patron que CARATULAS_ICONICAS en content_data.py)
    spotify_album_id = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'anio': self.anio,
            'titulo': self.titulo,
            'artista': self.artista,
            'descripcion': self.descripcion,
            'trivia': self.trivia,
            'imagen_url': self.imagen_url,
            'audio_url': self.audio_url,
            'spotify_album_id': self.spotify_album_id,
        }

    def __repr__(self):
        return f'<TimelineData {self.anio} - {self.titulo}>'
