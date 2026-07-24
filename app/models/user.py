# app/models/user.py

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=True) # Apodo o Usuario
    nombre_jugador = db.Column(db.String(100), nullable=True)     # Nombre completo para Leads
    email = db.Column(db.String(120), unique=True, nullable=True)
    whatsapp = db.Column(db.String(20), nullable=True)             # Teléfono para marketing
    password_hash = db.Column(db.String(256), nullable=True)       # Opcional si juegan sin registro tradicional
    
    score = db.Column(db.Integer, default=0)                       # Puntaje acumulado en trivias
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    acepta_promociones = db.Column(db.Boolean, default=True)        # Opt-in para promociones

    def set_password(self, password):
        """Genera el hash seguro de la contraseña."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña ingresada contra el hash guardado."""
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convierte el objeto a JSON para APIs de Leaderboard / Marketing."""
        return {
            'id': self.id,
            'nombre_jugador': self.nombre_jugador or self.username or 'Salsero Anónimo',
            'username': self.username or self.nombre_jugador or 'Anónimo',
            'email': self.email,
            'whatsapp': self.whatsapp,
            'score': self.score,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d %H:%M') if self.fecha_registro else ''
        }

    def __repr__(self):
        return f'<User {self.username or self.nombre_jugador}>'


class PageView(db.Model):
    __tablename__ = 'page_views'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<PageView {self.count}>'