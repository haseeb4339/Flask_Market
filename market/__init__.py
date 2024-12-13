from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

# Get the absolute path to the 'market/instance' directory
instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')

# Set the database URI to point to the correct location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(instance_path, 'market.db')

# Optional: Ensure the instance folder exists
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///market.db'

app.config['SECRET_KEY'] ='fb66252f3ca50d1173683580'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from market import routes