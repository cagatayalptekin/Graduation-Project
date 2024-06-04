# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query26


class TestFindMedian(unittest.TestCase):
    def test_find_median_with_even_length(self):
        self.assertEqual(query26.find_median([1, 3], [2, 4]), 2.5)

    def test_find_median_with_odd_length(self):
        self.assertEqual(query26.find_median([1, 3], [2]), 2.0)

    def test_find_median_with_empty_arrays(self):
        self.assertIsNone(query26.find_median([], []))

    def test_find_median_with_one_empty_array(self):
        self.assertEqual(query26.find_median([1, 2, 3], []), 2.0)
        self.assertEqual(query26.find_median([], [1, 2, 3, 4]), 2.5)

    def test_find_median_with_single_element_arrays(self):
        self.assertEqual(query26.find_median([1], [2]), 1.5)
    

    
        


if __name__ == '__main__':
    unittest.main()
