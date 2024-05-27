import unittest
from primes import is_prime

class PrimesTest(unittest.TestCase):

    def test1(self):
        """ check 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test2(self):
        """ check 2 is prime"""
        self.assertTrue(is_prime(2))

    def test3(self):
        """ check 3 is prime"""
        self.assertTrue(is_prime(3))

    def test4(self):
        """ check 4 is not prime"""
        self.assertFalse(is_prime(4))

    def test5(self):
        """ check 23 is prime"""
        self.assertTrue(is_prime(23))

if __name__ == "__main__":
    unittest.main()