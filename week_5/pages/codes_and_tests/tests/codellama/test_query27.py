# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query27

class TestMaxWater(unittest.TestCase):
    def test_max_water_with_varied_heights(self):
        self.assertEqual(query27.max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 16)

    def test_max_water_with_monotonic_increase(self):
        self.assertEqual(query27.max_water([1, 2, 3, 4, 5, 6, 7, 8, 9]), 20)

    def test_max_water_with_monotonic_decrease(self):
        self.assertEqual(query27.max_water([9, 8, 7, 6, 5, 4, 3, 2, 1]), 20)

    def test_max_water_with_single_element(self):
        self.assertEqual(query27.max_water([5]), 0)

    def test_max_water_with_two_elements(self):
        self.assertEqual(query27.max_water([1, 2]), 1)

    
        


if __name__ == '__main__':
    unittest.main()
