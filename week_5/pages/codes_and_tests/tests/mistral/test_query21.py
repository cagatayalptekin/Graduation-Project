# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from mistral import query21


class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring_with_unique_characters(self):
        self.assertEqual(query21.longest_substring("abcdef"), 6)

    def test_longest_substring_with_repeating_characters(self):
        self.assertEqual(query21.longest_substring("abcabcbb"), 3)

    def test_longest_substring_with_single_character(self):
        self.assertEqual(query21.longest_substring("bbbbbb"), 1)

    def test_longest_substring_with_empty_string(self):
        self.assertEqual(query21.longest_substring(""), 0)

    def test_longest_substring_with_mixed_characters(self):
        self.assertEqual(query21.longest_substring("pwwkew"), 3)
    

    
        


if __name__ == '__main__':
    unittest.main()
