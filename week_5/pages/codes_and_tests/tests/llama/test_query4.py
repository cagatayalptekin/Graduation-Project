# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query4


class TestQuery4(unittest.TestCase):
    def test_single_digit(self):
        self.assertTrue(query4.checkPalindrome(7))

    def test_positive_palindrome(self):
        self.assertTrue(query4.checkPalindrome(121))

    def test_negative_palindrome(self):
        self.assertFalse(query4.checkPalindrome(-121))



    def test_large_palindrome(self):
        self.assertTrue(query4.checkPalindrome(123454321))

    def test_large_non_palindrome(self):
        self.assertFalse(query4.checkPalindrome(123456789))
    


if __name__ == '__main__':
    unittest.main()
