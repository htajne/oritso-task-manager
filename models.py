from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(50), default='Pending')
    remarks = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(100), default=lambda: os.getenv('DEFAULT_USER', 'Gaurav'))
    updated_by = db.Column(db.String(100), default=lambda: os.getenv('DEFAULT_USER', 'Gaurav'))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'status': self.status,
            'remarks': self.remarks,
            'created_on': self.created_on.isoformat(),
            'updated_on': self.updated_on.isoformat(),
            'created_by': self.created_by,
            'updated_by': self.updated_by
        }
