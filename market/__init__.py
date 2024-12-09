from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

Flask_DEBUG = 1
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes