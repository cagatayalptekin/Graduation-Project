# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query20


class TestFindInsertionIndex(unittest.TestCase):
    def test_insertion_index_existing_element(self):
        self.assertEqual(query20.find_insertion_index([1, 3, 5, 6], 5), 2)

    def test_insertion_index_new_element_in_middle(self):
        self.assertEqual(query20.find_insertion_index([1, 3, 5, 6], 2), 1)

    def test_insertion_index_new_element_at_start(self):
        self.assertEqual(query20.find_insertion_index([1, 3, 5, 6], 0), 0)

    def test_insertion_index_new_element_at_end(self):
        self.assertEqual(query20.find_insertion_index([1, 3, 5, 6], 7), 4)

    def test_insertion_index_empty_array(self):
        self.assertEqual(query20.find_insertion_index([], 5), 0)
    

    
        


if __name__ == '__main__':
    unittest.main()
