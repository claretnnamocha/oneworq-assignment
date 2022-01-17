from datetime import datetime

from src.models import db


class ItemCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.DateTime, onupdate=datetime.now(), default=datetime.now())

    def __repr__(self) -> str:
        return f"{self.title}"

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "createdAt": self.createdAt.strftime("%a, %d %B %Y %H:%M:%S GMT"),
            "updatedAt": self.updatedAt.strftime("%a, %d %B %Y %H:%M:%S GMT"),
        }
