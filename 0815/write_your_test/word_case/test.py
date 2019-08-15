import unittest
from word_case import isupper
from word_case import islower


class TestLetterCase(unittest.TestCase):

    def test_isupper_all_upper(self):
        self.assertTrue(isupper('FOO'))

    # Can you think of other test cases for is upper? (hint: mix of upper and lower?)

    def test_islower_all_lower(self):
        self.assertTrue(islower('foo'))

    # Can you think of other test cases for islower ? (hint: mix of upper and lower?)

    def test_ismixed(self):
        # Can you think of your test cases for ismixed?
        pass

    # How many test cases can you creat for ismixed?

if __name__ == '__main__':
    unittest.main()
