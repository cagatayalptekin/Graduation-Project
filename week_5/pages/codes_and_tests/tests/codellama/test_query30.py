# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query30


class TestTrappingWater(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(query30.trapping_water([1]), 0)


    def test_flat_surface(self):
        self.assertEqual(query30.trapping_water([3, 3, 3, 3]), 0)

    def test_simple_case(self):
        self.assertEqual(query30.trapping_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


    def test_valley(self):
        self.assertEqual(query30.trapping_water([5, 2, 1, 2, 5]), 8)

    def test_complex_case(self):
        self.assertEqual(query30.trapping_water([4, 2, 0, 3, 2, 5]), 9)
    

    
        


if __name__ == '__main__':
    unittest.main()
