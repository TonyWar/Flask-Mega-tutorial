from flask import Flask
from config import Config

# __name__ - переопределённая переменная python,
# задаётся именем модуля, в котором используется
app = Flask(__name__)
app.config.from_object(Config)

# Импорт в конце чтобы избежать циклического импорта
from app import routes