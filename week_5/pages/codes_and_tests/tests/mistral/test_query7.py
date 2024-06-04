import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from mistral import query7



class TestQuery7(unittest.TestCase):
    def test_armstrong_number(self):
        # Test cases for Armstrong numbers
        self.assertEqual(query7.armstrongNumber(153), True)
    
    def test_armstrong_number_2(self):
        self.assertEqual(query7.armstrongNumber(9474), True)

    def test_non_armstrong_number(self):
        # Test cases for non-Armstrong numbers
        self.assertEqual(query7.armstrongNumber(123), False)
    
    def test_non_armstrong_number_2(self):
        self.assertEqual(query7.armstrongNumber(9475), False)

    def test_edge_cases(self):
        # Test cases for edge cases such as single digit numbers and zero
        self.assertEqual(query7.armstrongNumber(0), True)
        self.assertEqual(query7.armstrongNumber(1), True)
        self.assertEqual(query7.armstrongNumber(2), True)

if __name__ == '__main__':
    unittest.main()