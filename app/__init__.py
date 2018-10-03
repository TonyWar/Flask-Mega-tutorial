from flask import Flask

# __name__ - переопределённая переменная python,
# задаётся именем модуля, в котором используется
app = Flask(__name__)


# Импорт в конце чтобы избежать циклического импорта
from app import routes