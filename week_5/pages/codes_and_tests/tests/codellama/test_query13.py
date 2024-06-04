# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query13


class TestPrimeFactors(unittest.TestCase):
    def test_factors_of_one(self):
        result = query13.prime_factors(1)
        self.assertEqual(result, [])

    def test_factors_of_prime_number(self):
        result = query13.prime_factors(13)
        self.assertEqual(result, [13])

    def test_factors_of_small_composite_number(self):
        result = query13.prime_factors(12)
        self.assertEqual(result, [2, 2, 3])

    def test_factors_of_larger_composite_number(self):
        result = query13.prime_factors(90)
        self.assertEqual(result, [2, 3, 3, 5])

    def test_factors_of_perfect_square(self):
        result = query13.prime_factors(36)
        self.assertEqual(result, [2, 2, 3, 3])
    

    
        


if __name__ == '__main__':
    unittest.main()
