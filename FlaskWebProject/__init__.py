"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask.logging import create_logger
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
LOG.addHandler(streamHandler)

app.logger.setLevel(logging.INFO) 
 
file_handler = logging.FileHandler('login.log')
file_handler.setLevel(logging.INFO)  
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))
app.logger.addHandler(file_handler)
 
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) 
console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))
app.logger.addHandler(console_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
