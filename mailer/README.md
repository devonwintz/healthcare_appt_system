# Mailer

## Table of Contents
* [General Informaion](#general-info)
* [Setup](#setup)
* [Contributing](#contributing)
* [Support](#support) <br><br>


## General Information <a id="general-info"></a>
This *mailer* application was developed using the **Flask-Mail** extension, together with **RabbitMQ** message broker.

## Setup <a id="setup"></a>
To successfully run this application, both the Flask app and RabbitMQ (consumer) need to be running.
```
$ . .venv/bin/activate
$ python app.py
$ python consumer/consumer.py
```

## Contributing <a id="contributing"></a>
Contributions to this project should **not** be made on the **main** branch. As such, before you start making changes, you must first create a dedicated branch.
```
$ git checkout -b <branch-name>
```

### Committing Changes
Before you commit your changes. Run the following command to update the requirements.txt file.
```
$ pip freeze | sed 's/==.*$/''/' > requirements.txt
```

## Support <a id="support"></a>
* [Flask Official Documentation](https://flask.palletsprojects.com/en/2.2.x/)
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* [RabbitMQ Python](https://www.rabbitmq.com/tutorials/tutorial-one-python.htmls)
