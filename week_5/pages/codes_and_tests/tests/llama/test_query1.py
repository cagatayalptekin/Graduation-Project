# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query1


class TestQuery1(unittest.TestCase):
    def test_returns_zero_when_n_is_zero(self):
        result = query1.fib(0)
        self.assertEqual(result, 0)

    def test_returns_one_when_n_is_one(self):
        result = query1.fib(1)
        self.assertEqual(result, 1)

    def test_returns_correct_value_for_n_7(self):
        result = query1.fib(7)
        self.assertEqual(result, 13)
    #test_returns_correct_value_for_n_15
    def test_returns_correct_value_for_n_15(self):
        result = query1.fib(15)
        self.assertEqual(result, 610)
    def test_returns_correct_value_for_n_30(self):
        result = query1.fib(30)
        self.assertEqual(result, 832040)
    

    
        


if __name__ == '__main__':
    unittest.main()
