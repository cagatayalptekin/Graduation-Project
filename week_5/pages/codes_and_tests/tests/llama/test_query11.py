# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query11


class TestSecondLargest(unittest.TestCase):
    def test_returns_none_for_empty_list(self):
        result = query11.second_largest([])
        self.assertIsNone(result)

    def test_returns_none_for_single_element_list(self):
        result = query11.second_largest([5])
        self.assertIsNone(result)

    def test_returns_second_largest_when_first_element_is_largest(self):
        result = query11.second_largest([10, 3, 5, 2])
        self.assertEqual(result, 5)

    def test_returns_second_largest_when_first_element_is_not_largest(self):
        result = query11.second_largest([2, 13, 5, 7])
        self.assertEqual(result, 7)

    def test_returns_none_when_all_elements_are_same(self):
        result = query11.second_largest([7, 7, 7, 7])
        self.assertIsNone(result)
    

    
        


if __name__ == '__main__':
    unittest.main()
