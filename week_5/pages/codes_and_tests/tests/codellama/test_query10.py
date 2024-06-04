# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query10


class TestMergeSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        result = query10.merge_sort(arr)
        self.assertEqual(result, [])

    def test_single_element(self):
        arr = [1]
        result = query10.merge_sort(arr)
        self.assertEqual(result, [1])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        result = query10.merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        result = query10.merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random_order_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = query10.merge_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    

    
        


if __name__ == '__main__':
    unittest.main()
