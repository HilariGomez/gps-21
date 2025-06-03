"""Tests CI/CD"""

import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """Test Class"""

    def test_is_upper(self):
        """Returns true if a string is upper case"""
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """Returns true if a string is lower case"""
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """Returns true if a string starts with a capital letter"""
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
