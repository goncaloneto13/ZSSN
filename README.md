# ZSSN Rede Social de Sobrevivência Zumbi

## Prerequisites

* PostgreSQL 14 or newer.
https://www.postgresql.org/download/
* Django 3.2.13 or newer.
* Python 3.7 or newer.

## Configuring Postgres

### Register Server

![image](https://user-images.githubusercontent.com/28533981/163690323-754732ac-d44b-443b-8169-98c607ab8197.png)

### Name example: ```Teste```

![image](https://user-images.githubusercontent.com/28533981/163691478-94d6f826-0009-4b09-a725-5240534b504c.png)


### Host name/address: ```localhost```
### Username: ```postgres```

![image](https://user-images.githubusercontent.com/28533981/163691491-6d238c21-06cb-4291-914c-41c6f3f80655.png)

### Create Database:
![image](https://user-images.githubusercontent.com/28533981/163690346-60370222-793d-486c-a76c-9ad227950e57.png)
### Database: ```ZSSN```

![image](https://user-images.githubusercontent.com/28533981/163691465-677632c7-c034-4ec8-a309-7c2200212961.png)




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

4. Edit database user password in ```/ZSSN/settings.py```:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ZSSN',
        'USER':'postgres',
        'PASSWORD': 'db_user_password', #database user password
        'HOST': 'localhost'
    }
}
```

5. Create the DB tables:

```
python manage.py makemigrations
python manage.py migrate
```
5. Run Server:
```
python manage.py runserver
```
Development server at  http://localhost:8000/

