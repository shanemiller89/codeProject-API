# code.Project API

Rest API for code.Project

***BEFORE YOU START***, please make sure you have Python 3.7 or greater installed.

Clone Client side application and follow instructions. [Here](https://github.com/shanemiller89/codeproject)

Clone this repository down in desired location:

```
git@github.com:shanemiller89/codeProject-API.git
```

Enter these commands:

```
cd codeproject_API
python -m venv codeprojectEnv
source ./codeprojectEnv/bin/activate
```
Then run 

```
pip install -r requirements.txt
```

After installs are complete, run the following commands, in order.

```
python manage.py makemigrations codeprojectAPIapp
python manage.py migrate
python manage.py loaddata tasks_types
python manage.py loaddata technology_types
python manage.py loaddata supplemental_types
python manage.py runserver
```

Your code.Project API server is now up and running!

Run
```
python manage.py runserver
```
Each time you are using the application.

