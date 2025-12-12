'''coderadi &bull; All database models for the Project.'''

# ? IMPORTING LIBRARIES
from plugins import *

# | USER DATABASE MODEL
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(48), nullable=False)
    name = db.Column(db.String(48), nullable=False)
    email = db.Column(db.String(96), nullable=False)
    password = db.Column(db.String(12), nullable=False)