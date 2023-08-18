import unittest
from solution import sum_array

class TestSumArray(unittest.TestCase):

    def test_normal_list(self):
        self.assertEqual(sum_array([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_array([10, 20, 30]), 60)

    def test_empty_list(self):
        self.assertEqual(sum_array([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_array([-1, -2, 3, 4]), 4)
        self.assertEqual(sum_array([-10, 10]), 0)

    def test_large_list(self):
        self.assertEqual(sum_array(list(range(1, 10001))), 50005000)

if __name__ == "__main__":
    unittest.main()
