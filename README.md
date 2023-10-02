# niksari-backend
Enviroment installation for Windows:

1. Download env -file from Teams files
2. rename env file to .env file
3. Copy .env file to niksari-backend rootfolder
4. Use command prompt and go to /niksari-backend
5. Type Set-ExecutionPolicy Unrestricted -Scope Process
6. Type python -m venv env
7. To activate env type env/Scripts/activate
8. After that install dependencies by typing pip install -r requirements.txt
9. Start server by typing python manage.py runserver
