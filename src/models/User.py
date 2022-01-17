from datetime import datetime

import bcrypt
from src.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    hash = db.Column(db.Text(), nullable=False)
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.DateTime, onupdate=datetime.now(), default=datetime.now())

    @property
    def password(self):
        return self.hash

    @password.setter
    def password(self, password: str):
        self.hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode("utf-8")

    def validatePassword(self, password: str):
        return bcrypt.checkpw(password.encode(), self.hash.encode())

    def __repr__(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "createdAt": self.createdAt.strftime("%a, %d %B %Y %H:%M:%S GMT"),
            "updatedAt": self.updatedAt.strftime("%a, %d %B %Y %H:%M:%S GMT"),
        }
