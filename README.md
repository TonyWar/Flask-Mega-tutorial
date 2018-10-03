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

### Запуск приложения
1. Сообщаем FLASK как импортировать приложение
```
export FLASK_APP=manage.py
```
2. Запускаем
```
flask run
```