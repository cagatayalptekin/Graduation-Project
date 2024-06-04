# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query3


class TestQuery3(unittest.TestCase):
    def test_gcd_with_positive_numbers(self):
        self.assertEqual(query3.gcd(48, 18), 6)

    def test_gcd_with_zero(self):
        self.assertEqual(query3.gcd(0, 5), 5)
        self.assertEqual(query3.gcd(5, 0), 5)

    def test_gcd_with_negative_numbers(self):
        self.assertEqual(query3.gcd(-48, 18), 6)
        self.assertEqual(query3.gcd(48, -18), 6)

    def test_gcd_with_same_numbers(self):
        self.assertEqual(query3.gcd(10, 10), 10)

    def test_gcd_with_prime_numbers(self):
        self.assertEqual(query3.gcd(13, 17), 1)
    


if __name__ == '__main__':
    unittest.main()
