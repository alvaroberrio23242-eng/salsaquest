# app/models/visit_counter.py
"""Contador de visitas del sitio: una sola fila que se incrementa en
cada carga de la página principal."""

from app import db


class VisitCounter(db.Model):
    __tablename__ = 'visit_counter'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False, default=0)

    @classmethod
    def incrementar_y_obtener(cls):
        """Incrementa el contador (creándolo si no existe) y devuelve
        el total actualizado."""
        fila = cls.query.first()
        if fila is None:
            fila = cls(total=0)
            db.session.add(fila)
        fila.total += 1
        db.session.commit()
        return fila.total
