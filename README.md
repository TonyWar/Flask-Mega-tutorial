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

### Запуск приложения
1. Сообщаем FLASK как импортировать приложение
```
export FLASK_APP=manage.py
```
2. Запускаем
```
flask run
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

