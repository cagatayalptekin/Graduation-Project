# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query9


class TestRotateArray(unittest.TestCase):
    def test_no_rotation_when_n_is_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = 0
        result = query9.rotate_array(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_positive_rotation(self):
        arr = [1, 2, 3, 4, 5]
        n = 2
        result = query9.rotate_array(arr, n)
        self.assertEqual(result, [4, 5, 1, 2, 3])

    def test_negative_rotation(self):
        arr = [1, 2, 3, 4, 5]
        n = -2
        result = query9.rotate_array(arr, n)
        self.assertEqual(result, [3, 4, 5, 1, 2])

    def test_rotation_with_n_equal_to_length(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        result = query9.rotate_array(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_rotation_with_n_greater_than_length(self):
        arr = [1, 2, 3, 4, 5]
        n = 8
        result = query9.rotate_array(arr, n)
        self.assertEqual(result, [3, 4, 5, 1, 2])
    

    
        


if __name__ == '__main__':
    unittest.main()
