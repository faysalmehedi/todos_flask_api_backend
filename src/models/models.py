import bcrypt

from .base import BaseModel
from src.core.database import db 
# from core.database import db


class User(db.Model, BaseModel):

    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean)

    def __init__(self, name, email, password, admin=False, **kwargs):
        super(User, self).__init__(**kwargs)
        """Create a new user."""

        self.name = name
        self.email = email 
        self._password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.admin = admin

    def __repr__(self):
        return "User::{}".format(self.id)

    def check_password(self, password: str):
        return bcrypt.checkpw(password=password.encode(), hashed_password=self._password.encode())


class Todo(db.Model, BaseModel):

    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

    def __init__(self, text, complete, user_id, **kwargs):
        
        super(Todo, self).__init__(**kwargs)
        
        self.text = text 
        self.complete = complete 
        self.user_id = user_id

    def __repr__(self):
        return f"Todo::{self.id}"
