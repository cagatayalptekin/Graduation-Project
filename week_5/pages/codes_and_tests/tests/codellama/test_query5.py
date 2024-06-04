# test_query5.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query5


class TestFindMissingElements(unittest.TestCase):
    def test_empty_arrays(self):
        result = query5.find_missing_elements([], [])
        self.assertEqual(result, [])

    def test_no_missing_elements(self):
        result = query5.find_missing_elements([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, [])

    def test_all_elements_missing(self):
        result = query5.find_missing_elements([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])

    def test_some_elements_missing(self):
        result = query5.find_missing_elements([1, 2, 3, 4], [2, 4])
        self.assertEqual(result, [1, 3])

    def test_non_integer_elements(self):
        result = query5.find_missing_elements(['a', 'b', 'c'], ['a'])
        self.assertEqual(result, ['b', 'c'])
    

    
        


if __name__ == '__main__':
    unittest.main()
