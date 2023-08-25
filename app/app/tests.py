"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together"""
        result = calc.add(5, 8)

        self.assertEqual(result, 13)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        result = calc.subtract(15, 5)

        self.assertEqual(result, 10)        