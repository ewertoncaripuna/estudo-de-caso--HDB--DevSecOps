import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-padrao')

basedir = os.path.abspath(os.path.dirname(__file__))  # Isso aponta para a pasta onde está o __init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Always put Routes at end
from todo_project import routes
