# LaureatsBackEnd
Laureats Manager BackEnd REST Python
# LaureatsBackEnd
Laureats Manager BackEnd REST Python

Requirements :
1 -

pip install django 

pip install djangorestframework 

pip install pygments

2 -

Create Mysql db : laureats
Add PASSWORD in DATABASES =  (settings.py)

3-

change : (settings.py)
DEFAULT_FROM_EMAIL = 'example@gmail.com'
SERVER_EMAIL = 'example@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'password'

example@gmail.com to your email.
password to your email password.

3 - 
3-1-cd to project 

3-2-python manage.py makemigrations laureats

3-3-python manage.py migrate


4-
python manage.py runserver
