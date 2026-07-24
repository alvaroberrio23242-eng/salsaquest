# app/models/user.py

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    score = db.Column(db.Integer, default=0)  # Puntaje acumulado en las trivias

    def set_password(self, password):
        """Genera el hash seguro de la contraseña."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña ingresada contra el hash guardado."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class PageView(db.Model):
    __tablename__ = 'page_views'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<PageView {self.count}>'