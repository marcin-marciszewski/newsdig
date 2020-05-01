import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
import requests



app = Flask(__name__)

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

print(os.environ.get("GOOGLE_CLIENT_ID"))

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()



app.config['SECRET_KEY'] = 'mysecret'


############################
### DATABASE SETUP #########
############################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#########################
##### LOGIN CONFIGS #####
#########################Ad
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'
##################################################

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

from news.core.views import core
from news.users.views import users
from news.news_group.views import news_group





app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(news_group)


