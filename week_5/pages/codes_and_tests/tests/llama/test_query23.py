# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query23


class TestGetTriplets(unittest.TestCase):
    def test_triplets_with_positive_and_negative_numbers(self):
        self.assertCountEqual(query23.get_triplets([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

    def test_triplets_with_no_zero_sum(self):
        self.assertEqual(query23.get_triplets([1, 2, 3, 4, 5]), [])

    def test_triplets_with_multiple_zero_sum(self):
        self.assertCountEqual(query23.get_triplets([0, 0, 0, 0]), [[0, 0, 0]])

    def test_triplets_with_mixed_numbers(self):
        self.assertCountEqual(query23.get_triplets([-2, -1, 1, 2, 3, -3]), [[-2, -1, 3], [-3, 1, 2]])

    def test_triplets_with_empty_list(self):
        self.assertEqual(query23.get_triplets([]), [])

    
        


if __name__ == '__main__':
    unittest.main()
