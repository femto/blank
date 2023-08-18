import unittest
from solution import longest_palindromic_substring

class TestHardChallenge(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")
        self.assertEqual(longest_palindromic_substring("a"), "a")
        self.assertEqual(longest_palindromic_substring("ac"), "a")

if __name__ == '__main__':
    unittest.main()
