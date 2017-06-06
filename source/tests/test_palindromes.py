import unittest
from palindromes import *

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(isPalindrome('a'))

if __name__ == '__main__':
    unittest.main()