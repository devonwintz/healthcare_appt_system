from django.test import TestCase
from ...models import Appointment
from ...tests.fixtures import appointment


class AppointmentTestCase(TestCase):
    global appt
    appt = appointment()

    def test_string_representation(self):
        expected_str = f'Date: {appt.date}, Start Time: {appt.start_time}, End Time: {appt.end_time}'
        actual_str = str(appt)
        self.assertEqual(actual_str, expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Appointment._meta.verbose_name_plural), "appointments")
        
    def test_appointment_patient_relation(self):
        pass
    
    def test_appointment_doctor_relation(self):
        pass

    # Date
    def test_apptointment_date_not_null(self):
        self.assertNotEqual(appt.date, "")

    # Start Time
    def test_appointment_start_time_not_null(self):
        self.assertNotEqual(appt.start_time, "")

    # End Time
    def test_appointment_end_time_not_null(self):
        self.assertNotEqual(appt.end_time, "")

    # Status
    def test_appointment_status_not_null(self):
        self.assertNotEqual(appt.status, "")

