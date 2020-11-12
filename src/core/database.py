from flask_sqlalchemy import SQLAlchemy 

from .flask_app import app 

db = SQLAlchemy(app)