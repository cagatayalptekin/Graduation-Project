# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from mistral import query12


class TestGetShortestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        result = query12.get_shortest_palindrome("")
        self.assertEqual(result, " ")

    def test_already_palindrome(self):
        result = query12.get_shortest_palindrome("aba")
        self.assertEqual(result, "aba")

    def test_single_character(self):
        result = query12.get_shortest_palindrome("a")
        self.assertEqual(result, "aa")

    def test_non_palindrome_string(self):
        result = query12.get_shortest_palindrome("abc")
        self.assertEqual(result, "abccba")

    def test_complex_case(self):
        result = query12.get_shortest_palindrome("abcd")
        self.assertEqual(result, "abdcdcba")
    

    
        


if __name__ == '__main__':
    unittest.main()
