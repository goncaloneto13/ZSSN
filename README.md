# ZSSN Rede Social de Sobrevivência Zumbi

## Prerequisites

* PostgreSQL 14 or newer.
https://www.postgresql.org/download/
* Django 3.2.13 or newer.
* Python 3.7 or newer.

## Configuring Database

In SQL Shell (psql):

1. Create Database:

 ```
 CREATE DATABASE ZSSN; 
 ```

## Getting started

1. Clone the repository:

```
git clone https://github.com/goncaloneto13/ZSSN.git
```

2. Create a virtual environment (in Windows CMD):
```
cd ZSSN
python -m venv venv
.\venv\Scripts\Activate
```

3. Install all the application's dependencies:

```
pip install -r requirements.txt
```

4. Edit database in ```/ZSSN/settings.py```:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zssn', #database name
        'USER':'postgres',  #database user
        'PASSWORD': 'db_user_password', #database user password
        'HOST': 'localhost' #database host
    }
}
```

5. Create the DB tables:

```
python manage.py migrate
```
5. Run Server:
```
python manage.py runserver
```
Development server at  http://localhost:8000/

## Run Test

```
python manage.py test
```


