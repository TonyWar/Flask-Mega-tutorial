# Flask-Mega-tutorial
learn

### Создание виртуальной среды
```
python3 -m venv venv
```
### Войти в виртуальную среду
```
source venv/bin/activate
```

### Установка нужных зависимостей (выполнять внутри виртуальной среды)
Установка Flask
```
pip install flask
```
Установка Flask WTF - для работы с WTF Forms
```
pip install flask-wtf
```
Установка SQLAlchemy
```
pip install flask-sqlalchemy
```
Установка flask-migrate
```
pip install flask-migrate
```
Установка flask-login - для хранения сессий
```
pip install flask-login
```

### Запуск приложения
1. Сообщаем FLASK как импортировать приложение
```
export FLASK_APP=manage.py
```
2. Запускаем
```
flask run
```

Для отладки в браузере включаем режим
```
export FLASK_DEBUG=1
```

Для отладки отправки email сообщений
```
python -m smtpd -n -c DebuggingServer localhost:8025
```
Либо можно использовать настоящий ящик
```
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-username>
export MAIL_PASSWORD=<your-gmail-password>
```

### Конфиги VS Code
Анализатор - flake8
Интерпретатор - выбрать тот что для виртуального окружения

### Работа с Alchemy
Создание репозитория миграций:
```
flask db init
```
Миграция баз данныз:
```
flask db migrate -m "users table"
flask db migrate -m "posts table"
```
Применение изменений:
```
flask db upgrade
```

### Тестирование
Запуск тестов:
```
python tests.py
```