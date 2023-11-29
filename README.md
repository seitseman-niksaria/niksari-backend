# niksari-backend

## ⚡️ Quickstart

To get started, follow these steps:

1. Clone the GitHub Repository

   ```
   git clone https://github.com/seitseman-niksaria/niksari-backend.git
   ```

2. Navigate to the project directory

   ```
   cd niksari-backend
   ```

3. Create virtual environment (You need to have Python 3 installed on you machine before this step)

   ```
   python -m venv env
   ```

4. Activate virtual environment

   Windows

   ```
   env\Scripts\activate
   ```

   On some windows machines this command will result in an error. If this happens, then you need to execute this command first:

   ```
   Set-ExecutionPolicy Unrestricted -Scope Process
   ```

   Linux/MacOS

   ```
   source env/bin/activate
   ```
   
5. Install packages with pip

   ```
   pip install -r requirements.txt
   ```

   :exclamation:If you are getting error because of psycopg2 on Linux/MacOS, you need to install PostgreSQL.
   In early development stage we are using SQLite, but we will migrate to the PostreSQL in a later development stage.

6. Start the server

   ```
   python manage.py runserver
   ```

:exclamation: Keep in mind!
For development server .env file is needed. You can download it from Teams files. Don't share it or push it to the GitHub repository!!!
Remember that it must begin with a dot and it goes in to the root directory of the project.


## Djando admin

Django admin is an automatically build site area that you can use to create, view, update, and delete records in a database.
In development stage you can login and manage records at:

```
http://127.0.0.1:8000/admin
```

For CRUD operations you need to authenticate as a superuser/admin.

## Django REST framework

Django REST framework is a powerful and flexible toolkit for building Web APIs.
At this point you don't need to authenticate to use it, but in a future you will also need a superuser/admin credentials.

You can access Api Root at

```
http://127.0.0.1:8000
```

You can access furniture models list at

```
http://127.0.0.1:8000/furniture-models/
```

This project is also published in Render:

```
https://niksari-backend.onrender.com/furniture-models/
```
