from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# __name__ - переопределённая переменная python,
# задаётся именем модуля, в котором используется
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# Импорт в конце чтобы избежать циклического импорта
from app import routes, models
