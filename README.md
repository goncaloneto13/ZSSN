# ZSSN Rede Social de Sobrevivência Zumbi

## Prerequisites

* PostgreSQL 14 or newer.
https://www.postgresql.org/download/
* Django 3.2.13 or newer.
* Python 3.7 or newer.

Edit ```settings.py```:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER':'dn_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'localhost'
    }
}
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

4. Create the DB tables:

```
python manage.py makemigrations
python manage.py migrate
```
5. Run Server:
```
python manage.py runserver
```
Development server at  http://localhost:8000/

