from flask import Blueprint, jsonify
from app.models.timeline_data import TimelineData
from app import db

timeline_bp = Blueprint('timeline', __name__)


@timeline_bp.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        eventos = TimelineData.query.order_by(TimelineData.anio.asc()).all()
        return jsonify([e.to_dict() for e in eventos])

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500