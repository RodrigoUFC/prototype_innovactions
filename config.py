import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:latersontia2@localhost/postgres'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hj3auqbg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 10, 'pool_recycle': 50}
app.config['SQLALCHEMY_POOL_PRE_PING'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
