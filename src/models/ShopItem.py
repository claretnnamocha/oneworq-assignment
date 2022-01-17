from datetime import datetime
from email.policy import default
from sqlalchemy.dialects import postgresql as pg

from src.models import db


class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    price = db.Column(db.Integer, nullable=False)
    categories = db.Column(db.PickleType())
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.DateTime, onupdate=datetime.now(), default=datetime.now())

    def __repr__(self) -> str:
        return f"{self.title} - ₦{self.price}"

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "owner_id": self.owner_id,
            "price": self.price,
            "categories": self.categories,
            "createdAt": self.createdAt.strftime("%a, %d %B %Y %H:%M:%S GMT"),
            "updatedAt": self.updatedAt.strftime("%a, %d %B %Y %H:%M:%S GMT"),
        }
