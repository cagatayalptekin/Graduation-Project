# test_query1.py
import sys
sys.path.append('../week_5/pages/codes_and_tests/codes')
import unittest
from llama import query25


class TestCanReachEnd(unittest.TestCase):
    def test_can_reach_end_with_reachable_path(self):
        self.assertTrue(query25.can_reach_end([2, 3, 1, 1, 4]))

    def test_can_reach_end_with_unreachable_path(self):
        self.assertFalse(query25.can_reach_end([3, 2, 1, 0, 4]))

    def test_can_reach_end_with_single_element(self):
        self.assertTrue(query25.can_reach_end([0]))

    def test_can_reach_end_with_large_jumps(self):
        self.assertTrue(query25.can_reach_end([10, 1, 1, 1, 1]))

    def test_can_reach_end_with_no_jumps(self):
        self.assertFalse(query25.can_reach_end([0, 2, 3]))
    

    
        


if __name__ == '__main__':
    unittest.main()
