import unittest
from validate_input_in_functions import score_input

class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(validate_input_in_functions.score_input('Math'),'Math')

    def test_score_input_test_score_valid(self):
        self.assertEqual(validate_input_in_functions.score_input('Math',33 ), 'Math:33')

    def test_score_input_test_score_below_range(self):
        self.assertEqual(validate_input_in_functions.score_input('Math', -34), 'Invalid test score, try again!')

    def test_score_input_test_score_above_range(self):
        self.assertEqual(validate_input_in_functions.score_input('Math',123 ), 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertEqual(validate_input_in_functions.score_input('Math',rt), 'Invalid test score, try again!')

    def test_score_input_invalid_message(self):
        self.assertEqual(validate_input_in_functions.score_input( 'Math', rt, 'Invalid test score, try again!'), 'Invalid test score, try again!')



if __name__ == '__main__':
    unittest.main()
