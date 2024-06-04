import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query6

class TestQuery6(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(query6.longest_common_substring("abcde", "abfde"), "ab")

    def test_no_common_substring(self):
        self.assertEqual(query6.longest_common_substring("abc", "def"), "")


    def test_substring_at_end(self):
        self.assertEqual(query6.longest_common_substring("xyzabc", "defabc"), "abc")

    def test_case_sensitivity(self):
        self.assertEqual(query6.longest_common_substring("abc", "ABC"), "")

    def test_empty_strings(self):
        self.assertEqual(query6.longest_common_substring("", ""), "")
        self.assertEqual(query6.longest_common_substring("abc", ""), "")
        self.assertEqual(query6.longest_common_substring("", "abc"), "")

if __name__ == "__main__":
    unittest.main()