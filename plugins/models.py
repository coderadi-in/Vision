'''coderadi &bull; All database models for the Project.'''

# ? IMPORTING LIBRARIES
from plugins import *

# | USER DATABASE MODEL
class User(db.Model, UserMixin):
    '''
    ## User database model
    Holds the data of user.
    '''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(48), nullable=False)
    username = db.Column(db.String(48), nullable=False)
    email = db.Column(db.String(96), nullable=False)
    password = db.Column(db.String(12), nullable=False)