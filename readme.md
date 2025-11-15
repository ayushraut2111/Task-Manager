Steps to run the project :-
    1. clone the repository
    2. create a virtual environment and then activate the virtual environment. - optional step but advised 
    3. go to the project directory and then install all the requirements from the requirements.txt file
    4. now the project requirements is complete, to run project follow the below steps
    5. first run the python manage.py migrate command , this command will create a db and migrates all the tables to it
    6. now create a superuser to login in django admin by command. - python manage.py createsuperuser
    7. after the superuser is created run the python server by running the command python manage.py runserver
    8. now go to the django admin and login by the created credentials
