__author__ = 'Philip'

import unittest

import leaderboard_cyclopeptide_sequencing

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual([], list(leaderboard_cyclopeptide_sequencing.sublists([])))
        self.assertListEqual([[3]], list(leaderboard_cyclopeptide_sequencing.sublists([3])))
        self.assertListEqual([], list(leaderboard_cyclopeptide_sequencing.sublists([4, 5])))

    # def test_something(self):
    #     leaderboard = set([(4,), (3,)])
    #     spectrum = [5, 4, 3]
    #     result = leaderboard_cyclopeptide_sequencing.cut(leaderboard, spectrum, 1)
    #     self.assertSetEqual(result, set([4, 5]))


if __name__ == '__main__':
    unittest.main()
