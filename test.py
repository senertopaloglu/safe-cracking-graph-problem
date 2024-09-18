import unittest
import solution


class TestCalc(unittest.TestCase):
    def test_0(self):  # test_ prefix is required to auto run test case
        hints = [
          (7, 1),
          (1, 8),
          (7, 8),
        ]
        self.assertEqual(solution.safe_cracking(hints), '718')

    def test_1(self):
        hints = [
          (3, 1),
          (4, 7),
          (5, 9),
          (4, 3),
          (7, 3),
          (3, 5),
          (9, 1),
        ]
        self.assertEqual(solution.safe_cracking(hints), '473591')

    def test_2(self):
        hints = [
          (2, 5),
          (8, 6),
          (0, 6),
          (6, 2),
          (0, 8),
          (2, 3),
          (3, 5),
          (6, 5),
        ]
        self.assertEqual(solution.safe_cracking(hints), '086235')

    def test_3(self):
        hints = [
          (0, 1),
          (6, 0),
          (1, 8),
        ]
        self.assertEqual(solution.safe_cracking(hints), '6018')

    def test_4(self):
        hints = [
          (8, 9),
          (4, 2),
          (8, 2),
          (3, 8),
          (2, 9),
          (4, 9),
          (8, 4),
        ]
        self.assertEqual(solution.safe_cracking(hints), '38429')