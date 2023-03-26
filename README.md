# Healthcare Appointment System
![image](https://user-images.githubusercontent.com/31863401/222171465-051e9bb4-5221-4119-b135-3f678960c2d2.png)

## Table of Contents
- [Healthcare Appointment System](#healthcare-appointment-system)
  - [Table of Contents](#table-of-contents)
  - [General Information ](#general-information-)
  - [Setup ](#setup-)
  - [Usage ](#usage-)
    - [Patient](#patient)
    - [Emergency Contact](#emergency-contact)
    - [Allergy](#allergy)
    - [Emergency Contact](#emergency-contact-1)
    - [Specialization](#specialization)
    - [Doctor](#doctor)
    - [Appointment](#appointment)
  - [Support ](#support-)

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

## Usage <a id="usage"></a>
**baseURL**: `https://devonwintz.pythonanywhere.com`

**Generating Access Token**

**URL**: `baseURL/auth-token/`

**Body**:
```
{
 "username": "user",
 "password": "userpassword"
}
```

### Patient
**POST**: `baseURL/patients/`

**Body**:
```
{
 "first_name": "Test",
 "last_name": "Patient",
 "sex": "M",
 "dob": "1996-07-29",
 "telephone": "5926000000",
 "email": "test@example.com",
 "address_line_1": "Some Street",
 "ward_village": "Village",
 "city": "Georgetown",
 "country": "Guyana"
}
```

**GET**: `baseURL/patients/` & `baseURL/patients/id`


**PUT**: `baseURL/patients/id`

**Body**:
```
{
 "first_name": "Updated",
 "last_name": "Patient",
 "sex": "M",
 "dob": "1996-07-29",
 "telephone": "5926000000",
 "email": "test@example.com",
 "address_line_1": "Some Street",
 "ward_village": "Village",
 "city": "Georgetown",
 "country": "Guyana"
}
```

**DELETE:** `baseURL/patients/id`

### Emergency Contact
**POST**: `baseURL/emergency-contacts/`

**Body**:
```
{
  "patient": [
      1
      ],
  "first_name": "Test",
  "last_name": "Name",
  "relationship": "Friend",
  "telephone": "5926000000",
  "email": "test@example.com"
}
```

**GET**: `baseURL/emergency-contacts/` & `baseURL/emergency-contacts/id`

**PUT**: `baseURL/emergency-contacts/id`

**Body**:
```
{
  "patient": [
      1
      ],
  "first_name": "Updated",
  "last_name": "Name",
  "relationship": "Friend",
  "telephone": "5926000000",
  "email": "test@example.com"
}
```

**DELETE**: `baseURL/emergency-contacts/id`


### Allergy
**POST**: `baseURL/allergies/`

**Body**:
```
{
  "patient": 1,
  "name": "Papular Urticaria",
  "symptom": "Papules, itching",
  "medication": "Mild topical steroids"
}
```

**GET**: `baseURL/allergies/` & `baseURL/allergies/id`

**PUT**: `baseURL/allergies/id`

**Body**:
```
{
  "patient": 1,
  "name": "Papular Urticaria",
  "symptom": "Papules, itching, redness",
  "medication": "Mild topical steroids"
}
```

**DELETE**: `baseURL/allergies/id`

### Emergency Contact
**POST**: `baseURL/emergency-contacts/`

**Body**:
```
{
  "patient": [
      1
      ],
  "first_name": "Test",
  "last_name": "Name",
  "relationship": "Friend",
  "telephone": "5926000000",
  "email": "test@example.com"
}
```

**GET**: `baseURL/emergency-contacts/` & `baseURL/emergency-contacts/id`

**PUT**: `baseURL/emergency-contacts/id`

**Body**:
```
{
  "patient": [
      1
      ],
  "first_name": "Updated",
  "last_name": "Name",
  "relationship": "Friend",
  "telephone": "5926000000",
  "email": "test@example.com"
}
```

**DELETE**: `baseURL/emergency-contacts/id`


### Specialization
**POST**: `baseURL/specializations/`

**Body**:
```
{
  "name": "Dentist"
}
```

**GET**: `baseURL/specializations/` & `baseURL/specializations/id`

**PUT**: `baseURL/specializations/id`

**Body**:
```
{
  "name": "Dentistry",
}
```

**DELETE**: `baseURL/specializations/id`

### Doctor
**POST**: `baseURL/doctors/`

**Body**:
```
{
"first_name": "Test",
"last_name": "Doctor",
"specialization": [1],
"telephone": "5926000000",
"email": "test@example.com"
}
```

**GET**: `baseURL/doctors/` & `baseURL/doctors/id`

**PUT**: `baseURL/doctors/id`

**Body**:
```
{
"first_name": "Updated",
"last_name": "Doctor",
"specialization": [1],
"telephone": "5926000000",
"email": "test@example.com"
}
```

**DELETE**: `baseURL/doctors/id`

### Appointment
**POST**: `baseURL/appointments/`

**Body**:
```
{
"patient": 1,
"doctor":1,
"date": "2022-12-29",
"start_time": "12:30:00",
"end_time": "13:30:00"
}
```

**GET**: `baseURL/appointments/` & `baseURL/appointments/id`

**PUT**: `baseURL/appointments/id`

**Body**:
```
{
"patient": 1,
"doctor":1,
"date": "2022-12-29",
"start_time": "12:30:00",
"end_time": "13:30:00"
}
```

**DELETE**: `baseURL/appointments/id`


## Support <a id="support"></a>
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Django REST Framework YouTube Tutorial](https://www.youtube.com/watch?v=i5JykvxUk_A)
* [Django Extensions (Generating ERD)](https://django-extensions.readthedocs.io/en/latest/)
* [Flask Official Documentation](https://flask.palletsprojects.com/en/2.2.x/)
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* [RabbitMQ Python](https://www.rabbitmq.com/tutorials/tutorial-one-python.htmls)

