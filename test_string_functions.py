import unittest
from more_functions import string_functions


class StringTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string('Lisa', 1), 'Lisa')


if __name__ == '__main__':
    unittest.main()
