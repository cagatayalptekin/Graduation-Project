# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query28


class TestLongestValidParentheses(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(query28.longest_valid_parentheses("()"), 2)

    def test_nested_parentheses(self):
        self.assertEqual(query28.longest_valid_parentheses("((()))"), 6)

    def test_unbalanced_parentheses(self):
        self.assertEqual(query28.longest_valid_parentheses("(()"), 2)

    def test_mixed_characters(self):
        self.assertEqual(query28.longest_valid_parentheses(")()())"), 4)

    def test_no_valid_parentheses(self):
        self.assertEqual(query28.longest_valid_parentheses("((("), 0)
    

    
        


if __name__ == '__main__':
    unittest.main()
