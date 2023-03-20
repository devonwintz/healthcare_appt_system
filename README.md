# Healthcare Appointment System
![image](https://user-images.githubusercontent.com/31863401/222171465-051e9bb4-5221-4119-b135-3f678960c2d2.png)

## Table of Contents
* [General Informaion](#general-info)
* [Setup](#setup)
* [Contributing](#contributing)
* [Support](#support) <br><br>

## General Information <a id="general-info"></a>
This is a simple Patient Appointment Scheduling System, that makes it easy for Service Providers to manage their Patients' appointments. The system features:
* Frontend - developed with React and Ant Design 
* Backend - developed with Django
* Mailer - a custom mailing app developed with Flask

## Setup <a id="setup"></a>
1. Install Pipenv if not already installed
```
$ pip install pipenv
```
2. Activate Virtual Environment
```
$ pipenv shell
```
3. Install app dependencies
```
$ pipenv install
```
4. Propagate changes made to DB models (or simply create migrations)
```
$ python manage.py makemigrations healthcare_system
$ python manage.py migrate
```
5. Start the development server
```
$ python manage.py runserver
```

Other commands

i. Generate ERD:
```
$ python manage.py graph_models -a > erd.dot
$ dot -Tpdf erd.dot -o erd.pdf
```
ii. Reset Database:
```
$ python  manage.py reset_db
$ python manage.py migrate
```
iii. Truncate Table:
 ```
 $ python manage.py truncate --apps healthcare_system --models table_name
```


## Support <a id="support"></a>
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Django REST Framework YouTube Tutorial](https://www.youtube.com/watch?v=i5JykvxUk_A)
* [Django Extensions (Generating ERD)](https://django-extensions.readthedocs.io/en/latest/)
* [Flask Official Documentation](https://flask.palletsprojects.com/en/2.2.x/)
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* [RabbitMQ Python](https://www.rabbitmq.com/tutorials/tutorial-one-python.htmls)

