from django.test import TestCase
from ...models import Patient
from ...tests.fixtures import patient


class PatientTestCase(TestCase):
    global pat
    pat = patient()

    def test_string_representation(self):
        expected_str = f'First Name: {pat.first_name}, Last Name: {pat.last_name}, DOB: {pat.dob}'
        actual_str = str(pat)
        self.assertEqual(actual_str, expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Patient._meta.verbose_name_plural), "patients")

    # First & last names
    def test_patient_name_not_null(self):
        self.assertNotEqual(pat.first_name, "")
        self.assertNotEqual(pat.last_name, "")

    # Sex
    def test_patient_sex_not_null(self):
        self.assertNotEqual(pat.sex, "")

    # DOB
    def test_patient_dob_not_null(self):
        self.assertNotEqual(pat.dob, "")

    # Telephone
    def test_patient_telephone_not_null(self):
        self.assertNotEqual(pat.telephone, "")

    # Address Line 1
    def test_patient_address_not_null(self):
        self.assertNotEqual(pat.address_line_1, "")

    # City
    def test_patient_city_not_null(self):
        self.assertNotEqual(pat.city, "")

    # Country
    def test_patient_country_not_null(self):
        self.assertNotEqual(pat.country, "")
