import unittest
from one import is_prime  

class TestIsPrimeFunction(unittest.TestCase):

    def test_negative_numbers(self):
        """Test that negative numbers return False."""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(-100))

    def test_zero(self):
        """Test that zero returns False."""
        self.assertFalse(is_prime(0))

    def test_one(self):
        """Test that one returns False (since 1 is not prime)."""
        self.assertFalse(is_prime(1))

    def test_two(self):
        """Test that two returns True (since 2 is the smallest prime)."""
        self.assertTrue(is_prime(2))

    def test_three(self):
        """Test that three returns True (since 3 is prime)."""
        self.assertTrue(is_prime(3))

    def test_four(self):
        """Test that four returns False (since 4 is not prime)."""
        self.assertFalse(is_prime(4))

    def test_large_prime(self):
        """Test that a large prime number returns True."""
        self.assertTrue(is_prime(7919))  

    def test_large_non_prime(self):
        """Test that a large non-prime number returns False."""
        self.assertFalse(is_prime(10000))  

if __name__ == '__main__':
    unittest.main()
