__author__ = 'Philip'

import unittest

import genome
import leaderboard_cyclopeptide_sequencing

class MyTestCase(unittest.TestCase):
    def test_sublists(self):
        self.assertEqual([[]], list(leaderboard_cyclopeptide_sequencing.sublists([])))
        self.assertEqual([[3]], list(leaderboard_cyclopeptide_sequencing.sublists([3])))
        self.assertEqual([[4], [5], [4, 5]], list(leaderboard_cyclopeptide_sequencing.sublists([4, 5])))
        self.assertEqual([[4], [5], [6], [4, 5], [5, 6], [6, 4], [4, 5, 6]],
                         list(leaderboard_cyclopeptide_sequencing.sublists([4, 5, 6])))

    def test_expand(self):
        leaderboard = {(0,)}
        result = leaderboard_cyclopeptide_sequencing.expand(leaderboard, set(genome.readUniqueWeights()))
        self.assertIn((0, 129), result)
        self.assertIn((0, 103), result)
        self.assertEqual(18, len(result))
        leaderboard = {(0, 129)}
        result = leaderboard_cyclopeptide_sequencing.expand(leaderboard, set(genome.readUniqueWeights()))
        self.assertIn((0, 129, 129), result)
        self.assertIn((0, 129, 103), result)
        self.assertEqual(18, len(result))

    def test_score(self):
        # leaderboard = {(0, 129), (0, 97), (0, 128)}
        # (0, 129), (0, 97), (0, 128), (0, 163), (0, 115), (0, 57), (0, 147), (0, 114), (0, 103),
        # (0, 113), (0, 101), (0, 71), (0, 137), (0, 131), (0, 156), (0, 99), (0, 87), (0, 186)
        spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
        peptide = (114, 128, 129, 113)
        self.assertEqual(11, leaderboard_cyclopeptide_sequencing.score(peptide, spectrum))

    def test_cut(self):
        leaderboard = {(4,), (3,)}
        spectrum = [5, 4, 3]
        result = leaderboard_cyclopeptide_sequencing.cut(leaderboard, spectrum, 1)
        self.assertEqual(result, set([4, 5]))



if __name__ == '__main__':
    unittest.main()
