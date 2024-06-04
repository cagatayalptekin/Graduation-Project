# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query2


class TestQuery2(unittest.TestCase):
    def test_returns_false_when_n_is_zero(self):
        result = query2.isPrime(0)
        self.assertFalse(result)

    def test_returns_false_when_n_is_one(self):
        result = query2.isPrime(1)
        self.assertFalse(result)

    def test_returns_true_for_prime_number_7(self):
        result = query2.isPrime(7)
        self.assertTrue(result)

    def test_returns_false_for_non_prime_number_15(self):
        result = query2.isPrime(15)
        self.assertFalse(result)

    def test_returns_true_for_prime_number_29(self):
        result = query2.isPrime(29)
        self.assertTrue(result)
    
    
 
    
        


if __name__ == '__main__':
    unittest.main()
