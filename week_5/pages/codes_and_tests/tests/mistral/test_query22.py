# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from mistral import query22


class TestIntToRoman(unittest.TestCase):
    def test_int_to_roman_basic_numbers(self):
        self.assertEqual(query22.int_to_roman(3), 'III')

    def test_int_to_roman_subtractive_notation(self):
        self.assertEqual(query22.int_to_roman(4), 'IV')
        self.assertEqual(query22.int_to_roman(9), 'IX')

    def test_int_to_roman_tens_and_units(self):
        self.assertEqual(query22.int_to_roman(58), 'LVIII')
        self.assertEqual(query22.int_to_roman(44), 'XLIV')

    def test_int_to_roman_hundreds_and_units(self):
        self.assertEqual(query22.int_to_roman(1994), 'MCMXCIV')
        self.assertEqual(query22.int_to_roman(2023), 'MMXXIII')

    def test_int_to_roman_thousands(self):
        self.assertEqual(query22.int_to_roman(3999), 'MMMCMXCIX')
    

    
        


if __name__ == '__main__':
    unittest.main()
