from flask import Flask, request
from flask_mail import Mail
from mail import Email
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(dotenv_path=find_dotenv())

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_PROVIDER_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PROVIDER_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_PROVIDER_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PROVIDER_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

print(os.environ.get('MAIL_SENDER'))


def send(data, emailType):
    if emailType == "notice":
        subject = os.environ.get('MAIL_NOTICE_SUBJECT')
    else:
        subject = os.environ.get('MAIL_REMINDER_SUBJECT')

    sender = os.environ.get('MAIL_SENDER')
    props = {
        "contact_email": os.environ.get('MAIL_CONTACT_EMAIL'),
        "contact_telephone": os.environ.get('MAIL_CONTACT_NUMBER'),
        "start_time": '{}:{}'.format(data['start_time'].split(':')[0], data['start_time'].split(':')[1]),
        "end_time": '{}:{}'.format(data['end_time'].split(':')[0], data['end_time'].split(':')[1]),
        "recipients": [data['patient']['email']],
        "cc": [data['doctor']['email']]
    }

    email = Email(data, **props)
    results = email.send(mail, subject, sender, props['recipients'], props['cc'], emailType)

    return results

@app.route("/appointment/<identifier>", methods=['POST'])
def post(identifier):
    data = request.json
    res = send(data, identifier)
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)