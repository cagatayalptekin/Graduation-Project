# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from codellama import query14


class TestCoinChange(unittest.TestCase):
    def test_amount_zero(self):
        result = query14.coin_change([1, 2, 5], 0)
        self.assertEqual(result, 0)  # 0 coins needed

    def test_achievable_amount(self):
        result = query14.coin_change([1, 2, 5], 11)
        self.assertEqual(result, 3)  # 5 + 5 + 1

    def test_unachievable_amount(self):
        result = query14.coin_change([2], 3)
        self.assertEqual(result, -1)  # Impossible with only 2-valued coins

    def test_single_coin_denomination(self):
        result = query14.coin_change([5], 15)
        self.assertEqual(result, 3)

    def test_larger_denominations(self):
        result = query14.coin_change([1, 5, 10, 25], 63)
        self.assertEqual(result, 3)  # 25 + 25 + 10 + 3
    

    
        


if __name__ == '__main__':
    unittest.main()
