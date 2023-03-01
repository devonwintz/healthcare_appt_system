from django.test import TestCase
from ...models import Specialization
from ...tests.fixtures import specialization


class SpecializationTestCase(TestCase):
    global spc
    spc = specialization()

    def test_string_representation(self):
        expected_str = f'Name: {spc.name}'
        actual_str = str(spc)
        self.assertEqual(actual_str, expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Specialization._meta.verbose_name_plural), "specializations")

    # Name
    def test_specialization_name_not_null(self):
        self.assertNotEqual(spc.name, "")


