import unittest
from solution import sum_two_numbers

class TestEasyChallenge(unittest.TestCase):

    def test_sum_two_numbers(self):
        self.assertEqual(sum_two_numbers(1, 2), 3)
        self.assertEqual(sum_two_numbers(-1, 2), 1)
        self.assertEqual(sum_two_numbers(1000, -1000), 0)

if __name__ == '__main__':
    unittest.main()
