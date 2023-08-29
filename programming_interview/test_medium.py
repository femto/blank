import unittest
from solution import fibonacci

class TestMediumChallenge(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(10), 34)

if __name__ == '__main__':
    unittest.main()
