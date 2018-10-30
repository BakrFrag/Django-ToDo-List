# Project Title

Django ToDo List App

# Project Description
simple ToDo List app Written In django

# Getting Started

git must be installed in your system

* [git version control](https://git-scm.com/) - git bash used to clone repos from github

open terminal paste the command below and press enter
```
git clone 
```
# Prerequisites

computer with operating system 

python interpeter installed on it 

prefered to use python 3.6 or higher version py_interperter>=3.6

# Installing

python interperter must be installed

open your terminal 

1.install pipenv package-manager with command 
 ```
pip install pipenv
```
2.install djnago with command
```
pip install django
```

# Running the project

1.active pipenv by command 
```
 pipenv shell
 ```
2. navigate to todo folder
```
cd todo
```
3. run following commands in order
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py collectstatic
```
```
python manage.py runserver
```
# Attenation
in settings.py file 
put you own email on EMAIL_HOST_USER
put you own password on EMAIL_HOST_PASSWORD
the configrations used in the project not suitable for real world DEPLOYMENT
it's only used in DEVELOPMENT MODE not PRODUCTION MODE

# Build With

* [python](https://www.python.org/) - The web framework used
* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [Google Fonts](https://fonts.google.com/) - The Front End Library Used