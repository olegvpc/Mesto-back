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

python manage.py makemigrations <APPS>

python manage.py migrate <APPS>

Создание admin
python manage.py createsuperuser

АУТЕНТИФИКАЦИЯ

```python
pip install djoser djangorestframework_simplejwt 
PyJWT==1.7.1 
```
```
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ]
# }
# POST запрос на http://127.0.0.1:8000/api-token-auth/
#
# {
#     "username": "oleg",
#     "password": "12345poiuy"
# }
# ответ
# {
#     "token": "26d52d2a673416f7a624ef7a10a2aa62aa85f383"
# }
#
# Более продвитнутый токен -JSON Web Token
# можно СОЗДАВАТЬ новых пользователей через
# POST запрос на http://127.0.0.1:8000/v1/auth/users/
{
    "username": "nadin",
    "password": "12345poiuy"
}

# ответ {
#     "email": "",
#     "username": "nadin",
#     "id": 4
# }

# далее получаем новый Token - Bearer для пользователя
# по POST запросу
# http://127.0.0.1:8000/auth/jwt/create/


# в виде
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1ODY3MzkxOCwianRpIjoiZmM2Y2RmMjhmNzdjNGM5ZTg1ZjUxMGYxMDA5NTY1YzMiLCJ1c2VyX2lkIjo0fQ.bjuUT3ONyyU7smsNQKYEjRexL6NWu6tQuL853r7ZuVQ",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MjI3NTE4LCJqdGkiOiI1NjNhOWZiZmFkYjA0MjQ3ODM2ZGUzODdiZjBmNGM5OSIsInVzZXJfaWQiOjR9.g2-i-ZVUJJHLtdVP86QJ_e-YFT9OAhaXUZGuBWnozKY"
}
``` python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```
#
```
```SIMPLE_JWT = {
    # Устанавливаем срок жизни токена
   'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
   'AUTH_HEADER_TYPES': ('Bearer',),
}
```
CORS - блокировки при деплое проекта на удаленном сервере
```python
pip install django-cors-headers
pip install django-utils-six
```

