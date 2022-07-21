# Mesto-back
### back-end for project Mesto

python3 -m venv venv
source venv/bin/activate 

pip install Django

- создание директории с проектом
django-admin startproject название_проекта 
- создание приложения
python manage.py startapp firstapp

Первый запуск сервера
python3 manage.py runserver


Создание требований
 pip freeze > requirements.txt 

pip install -r requirements.txt

для работы с запросами request 
pip install requests


Создание и запуск скриптов миграции

python manage.py makemigrations

python manage.py migrate  

Создание admin
python manage.py createsuperuser

