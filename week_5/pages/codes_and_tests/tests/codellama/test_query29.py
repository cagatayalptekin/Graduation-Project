# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query29


class TestSearchNumberInRotatedSortedArray(unittest.TestCase):
    def test_target_in_left_half(self):
        self.assertEqual(query29.search_number_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 5), 1)

    def test_target_is_pivot(self):
        self.assertEqual(query29.search_number_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_target_not_found(self):
        self.assertEqual(query29.search_number_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_single_element_found(self):
        self.assertEqual(query29.search_number_in_rotated_sorted_array([1], 1), 0)

    def test_single_element_not_found(self):
        self.assertEqual(query29.search_number_in_rotated_sorted_array([1], 0), -1)
    

    
        


if __name__ == '__main__':
    unittest.main()
