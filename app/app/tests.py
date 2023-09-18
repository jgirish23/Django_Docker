""""
test cal
"""

from django.test import SimpleTestCase
from app import cal

class CalTests(SimpleTestCase):
    """Test the cal module."""

    def test_add_numbers(self):
        """adding 2 numbers"""

        res=cal.add(5,4)

        self.assertEqual(res,9)

    def test_subtract_numbers(self):
        """subtracting 2 numbers"""
        res=cal.sub(5,4)

        self.assertEqual(res,1)