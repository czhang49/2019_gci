import unittest
from contain_duplicates import has_duplicates

class TestDuplicates(unittest.TestCase):

    def test_duplicates(self):
        self.assertTrue(has_duplicates("abccba"))

    # Can you think of other test cases? What if I consider upper case and lower
    # case letter to be the same letter?

    # Have you considered numbers? Symbols?


if __name__ == '__main__':
    unittest.main()
