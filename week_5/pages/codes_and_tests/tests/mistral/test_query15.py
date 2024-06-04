# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from mistral import query15


class TestSuperPalindromes(unittest.TestCase):
    def test_small_range(self):
        result = query15.count_super_palindromes("1", "9")
        self.assertEqual(result, 3)  # 1, 4, 9 

    def test_range_with_larger_values(self):
        result = query15.count_super_palindromes("400", "1000")
        self.assertEqual(result, 2)  # 484 (sqrt 22)

    def test_left_boundary(self):
        result = query15.count_super_palindromes("4", "20")
        self.assertEqual(result, 2)  # As above

    def test_right_boundary(self):
        result = query15.count_super_palindromes("80", "121")
        self.assertEqual(result, 1)  #  121 (sqrt 11)

    def test_single_value_range(self):
        result = query15.count_super_palindromes("121", "121")
        self.assertEqual(result, 1)
    

    
        


if __name__ == '__main__':
    unittest.main()
