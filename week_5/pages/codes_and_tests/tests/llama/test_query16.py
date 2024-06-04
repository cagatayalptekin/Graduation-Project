# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query16


class TestTwoSum(unittest.TestCase):
    def test_two_sum_with_positive_numbers(self):
        self.assertEqual(query16.two_sum([2, 7, 11, 15], 9), [0, 1])
        

    def test_two_sum_with_no_solution(self):
        self.assertEqual(query16.two_sum([1, 2, 3], 7), [])
        

    def test_two_sum_with_negative_numbers(self):
        self.assertEqual(query16.two_sum([-1, -2, -3, -4, -5], -8), [2, 4])
        

    def test_two_sum_with_duplicates(self):
        self.assertEqual(query16.two_sum([3, 3], 6), [0, 1])
        

    def test_two_sum_with_single_element(self):
        self.assertEqual(query16.two_sum([1], 2), [])
        
    

    
        


if __name__ == '__main__':
    unittest.main()
