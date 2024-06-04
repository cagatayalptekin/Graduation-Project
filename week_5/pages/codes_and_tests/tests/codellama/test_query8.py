# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query8


class TestBalancedParentheses(unittest.TestCase):
    def test_empty_string(self):
        result = query8.balanced_parentheses("")
        self.assertTrue(result)

    def test_balanced_parentheses(self):
        result = query8.balanced_parentheses("({[]})")
        self.assertTrue(result)

    def test_balanced_parentheses2(self):
        result = query8.balanced_parentheses("({[})]")
        self.assertFalse(result)

    def test_missing_closing(self):
        result = query8.balanced_parentheses("({[}")
        self.assertFalse(result)

    def test_extra_closing(self):
        result = query8.balanced_parentheses("({[]})]")
        self.assertFalse(result)
    

    
        


if __name__ == '__main__':
    unittest.main()
