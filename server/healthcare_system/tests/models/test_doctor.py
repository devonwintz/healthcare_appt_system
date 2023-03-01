from django.test import TestCase
from ...models import Doctor
from ...tests.fixtures import doctor


class DoctorTestCase(TestCase):
    global doc
    doc = doctor()

    def test_string_representation(self):
        expected_str = f"First Name: {doc.first_name}, Last Name: {doc.last_name}, Specialization: {doc.specialization.values_list('name', flat=True)}"
        actual_str = str(doc)
        self.assertEqual(actual_str, expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Doctor._meta.verbose_name_plural), "doctors")

    # First & last names
    def test_doctor_name_not_null(self):
        self.assertNotEqual(doc.first_name, "")
        self.assertNotEqual(doc.last_name, "")

    # Telephone
    def test_doctor_telephone_not_null(self):
        self.assertNotEqual(doc.telephone, "")

    # Specialization
    def test_doctor_address_not_null(self):
        self.assertNotEqual(doc.specialization, "")