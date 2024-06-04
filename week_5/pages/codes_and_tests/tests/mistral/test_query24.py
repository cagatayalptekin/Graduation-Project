# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from mistral import query24


class TestThreeSumClosest(unittest.TestCase):
    def test_closest_sum_with_positive_numbers(self):
        self.assertEqual(query24.threeSumClosest([1, 2, 3, 4, 5], 10), 10)

    def test_closest_sum_with_negative_numbers(self):
        self.assertEqual(query24.threeSumClosest([-1, -2, -3, -4, -5], -10), -10)

    def test_closest_sum_with_mixed_numbers(self):
        self.assertEqual(query24.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_closest_sum_with_zero_target(self):
        self.assertEqual(query24.threeSumClosest([0, 2, 1, -3], 1), 0)

    def test_closest_sum_with_large_numbers(self):
        self.assertEqual(query24.threeSumClosest([100, 200, 300, 400], 800), 800)
    

    
        


if __name__ == '__main__':
    unittest.main()
    