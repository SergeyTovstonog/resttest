from django.test import TestCase

from .calc import add

class CalcTest(TestCase):

    def test_add_numbers(self):
        """Checking 2 numbers add are ok"""
        self.assertEqual(add(3, 8), 11)