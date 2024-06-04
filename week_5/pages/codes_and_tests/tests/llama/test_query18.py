# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query18


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_with_mixed_numbers(self):
        self.assertEqual(query18.remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_duplicates_with_all_unique(self):
        self.assertEqual(query18.remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_duplicates_with_all_duplicates(self):
        self.assertEqual(query18.remove_duplicates([2, 2, 2, 2, 2]), [2])

    def test_remove_duplicates_with_empty_list(self):
        self.assertEqual(query18.remove_duplicates([]), [])

    def test_remove_duplicates_with_strings(self):
        self.assertEqual(query18.remove_duplicates(['a', 'b', 'a', 'c', 'b']), ['a', 'b', 'c'])

    

    
        


if __name__ == '__main__':
    unittest.main()
