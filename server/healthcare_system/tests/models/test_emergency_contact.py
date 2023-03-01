from django.test import TestCase
from ...models import Emergency_Contact
from ...tests.fixtures import emergency_contact


class EmergencyContactTestCase(TestCase):
    global contact
    contact = emergency_contact()

    def test_string_representation(self):
        expected_str = f'First Name: {contact.first_name}, Last Name: {contact.last_name}, Relationship: {contact.relationship}'
        actual_str = str(contact)
        self.assertEqual(actual_str, expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Emergency_Contact._meta.verbose_name_plural), "emergency contacts")

        
    def test_emergency_contact_patient_relation(self):
        pass

    # First & last names
    def test_emergency_contact_name_not_null(self):
        self.assertNotEqual(contact.first_name, "")
        self.assertNotEqual(contact.last_name, "")

    # Relationship
    def test_emergency_contact_relationship_not_null(self):
        self.assertNotEqual(contact.relationship, "")

    # Telephone
    def test_emergency_contact_telephone_not_null(self):
        self.assertNotEqual(contact.telephone, "")

