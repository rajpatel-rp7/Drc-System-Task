# Drc-System-Task
### Steps to Run The Project
step 1: create virtual environment
-- python -m venv venv
step 2: install dependencies throw requirements.txt
-- pip install -r requirements.txt
step 3: make migrations 
-- python manage.py makemigrations
step 4: migrate
-- python manage.py migrate
step 5: createsuperuser
-- python manage.py createsuperuser
step 6: Runserver
-- python manage.py runserver


### Requirements
asgiref==3.2.10
Django==3.1.2
django-crispy-forms==1.9.2
django-progressbarupload==0.1.7
pytz==2020.1
sqlparse==0.4.1

