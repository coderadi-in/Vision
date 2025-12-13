'''coderadi &bull; Heart file of the Project.'''

# ? IMPORTING LIBRARIES
from flask import Flask
from plugins.models import *
import plugins
import os

# ? IMPORTING ROUTERS
from router.base import base_router
from router.auth import auth_router

# ! ───────────────────────────────┐
# ! LOADING ENVIRONMENT VARIABLES  │
from dotenv import load_dotenv   #!│
load_dotenv('.venv/vars.env')    #!│
# ! ───────────────────────────────┘

# ! BUILDING SERVER
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# ! BINDING PLUGINS
plugins.bind_plugins(server)

# ! BUILDING DATABASE
with (server.app_context()):
    plugins.db.create_all()

# ! BINDING ROUTERS
server.register_blueprint(base_router)
server.register_blueprint(auth_router)

# | USER LOADER
@plugins.logger.user_loader
def load_user(user):
    return User.query.get(user)