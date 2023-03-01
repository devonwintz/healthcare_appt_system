from django.test import TestCase
from ...models import Allergy
from ...tests.fixtures import allergy


class AllergyTestCase(TestCase):
    global algy
    algy = allergy()

    def test_string_representation(self):
        expected_str = f'Name: {algy.name}, Symptoms: {algy.symptom}'
        actual_str = str(algy)
        self.assertEqual(actual_str, expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Allergy._meta.verbose_name_plural), "allergies")
        
    def test_allergy_patient_relation(self):
        pass

    # Name
    def test_allergy_date_not_null(self):
        self.assertNotEqual(algy.name, "")

    # Symptoms
    def test_allergy_symptom_not_null(self):
        self.assertNotEqual(algy.symptom, "")

   