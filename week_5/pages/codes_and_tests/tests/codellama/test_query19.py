# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query19


class TestStrStr(unittest.TestCase):
    def test_strStr_with_existing_substring(self):
        self.assertEqual(query19.strStr("ll", "hello"), 2)

    def test_strStr_with_non_existing_substring(self):
        self.assertEqual(query19.strStr("world", "hello"), -1)

    def test_strStr_with_empty_needle(self):
        self.assertEqual(query19.strStr("", "hello"), 0)

    def test_strStr_with_empty_haystack(self):
        self.assertEqual(query19.strStr("hello", ""), -1)

    def test_strStr_with_needle_equal_haystack(self):
        self.assertEqual(query19.strStr("hello", "hello"), 0)
    

    
        


if __name__ == '__main__':
    unittest.main()
