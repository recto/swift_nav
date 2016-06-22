"""
Test case for application.py
"""
import sys
sys.path.append("../src")
import application
import unittest

class ApplicationTestCase(unittest.TestCase):
    """
        Test case for application module.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fib(self):
        """
            test case for application.fib(n).
        """
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(expected, application.fib(10))
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                987, 1597, 2584, 4181, 6765]
        self.assertEqual(expected, application.fib(20))

    def test_fib_overflow(self):
        """
            test case for application.fizz_buzz(n) when n is large and it
            overflows.
        """
        with self.assertRaises(OverflowError):
            application.fib(1000)

    def test_fizz_buzz(self):
        """
            test case for application.fizz_buzz(n).
        """
        expected = [0, 1, 1, "BuzzFizz", "Buzz", "Fizz", 8, "BuzzFizz", "Buzz",
            34, "Fizz"]
        self.assertEqual(expected, application.fizz_buzz(10))
        expected = [0, 1, 1, "BuzzFizz", "Buzz", "Fizz", 8, "BuzzFizz", "Buzz",
                34, "Fizz", "BuzzFizz", "Buzz", "BuzzFizz", 377, "Fizz", "Buzz",
                "BuzzFizz", 2584, 4181, "FizzBuzz"]
        self.assertEqual(expected, application.fizz_buzz(20))

    def test_fizz_buzz_overflow(self):
        """
            test case for application.fizz_buzz(n) when n is large and it
            overflows.
        """
        with self.assertRaises(SystemExit):
            application.fizz_buzz(100)

if __name__ == "__main__":
    unittest.main()

