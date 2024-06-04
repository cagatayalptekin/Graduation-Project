# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query17


class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int_with_basic_numerals(self):
        self.assertEqual(query17.roman_to_int("III"), 3)

    def test_roman_to_int_with_subtractive_notation(self):
        self.assertEqual(query17.roman_to_int("IV"), 4)

    def test_roman_to_int_with_combined_notation(self):
        self.assertEqual(query17.roman_to_int("MCMXCIV"), 1994)

    def test_roman_to_int_with_large_numerals(self):
        self.assertEqual(query17.roman_to_int("MMXXIV"), 2024)

    def test_roman_to_int_with_repeated_numerals(self):
        self.assertEqual(query17.roman_to_int("LVIII"), 58)
    

    
        


if __name__ == '__main__':
    unittest.main()
