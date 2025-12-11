'''coderadi &bull; Plugins file of the Project.'''

# ? IMPORTING LIBRARIES
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_migrate import Migrate, migrate
from flask_bcrypt import Bcrypt
from authlib.integrations.flask_client import OAuth

# ! BUILDING PLUGINS
db = SQLAlchemy()
logger = LoginManager()
upgrade = Migrate()
bcrypt = Bcrypt()
oauth = OAuth()

# * FUNCTION TO BIND PLUGINS TO SERVER
def bind_plugins(server):
    '''Binds all plugins to the server.'''

    db.init_app(server)
    logger.init_app(server)
    upgrade.init_app(server, db)
    bcrypt.init_app(server)
    oauth.init_app(server)

