from flask import render_template
from flask_mail import Message

class Email(object):
    def __init__(self, data, **props):
        self.props = {
        'patient_name': data['patient']['fullname'],
        'patient_email': data['patient']['email'],
        'doctor_name': data['doctor']['fullname'],
        'doctor_email': data['doctor']['email'],
        'appt_date': data['date'],
        'appt_start_time': props.get('start_time'),
        'appt_end_time': props.get('end_time'),
        'contact_email': props.get('contact_email'),
        'contact_telephone': props.get('contact_telephone')
        }
    
    def send(self, mail, subject, sender, recipients, cc, type):
        msg = Message(subject, sender=sender, recipients=recipients, cc=cc)
        if(type == 'notice'):
            msg.html = render_template('appointment_notification.html', **self.props)
        elif(type == 'reminder'):
            msg.html = render_template('appointment_reminder.html', **self.props)

        if(self.props['patient_email']):
            mail.send(msg)
            results = {
            'status': 'success',
            'message': 'Email was sent'
            }
            return results
        else:
            mail.send(msg)
            results = {
                'status': 'success',
                'message': 'No patient email was provided. Email was only sent to the doctor'
            }
            return results
        
