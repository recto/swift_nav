""" Fibonacci and FizzBuzz """
from __future__ import print_function
import sys
import math

def fib(nth):
    """
    Fibonacchi Number
    :param nth: nth
    :return: return n Fibonacchi numbers.
    """
    nums = [0, 1, 1]
    if nth == 0:
        return [0]
    elif nth == 1:
        return [0, 1]
    elif nth == 2:
        return nums
    for _ in xrange(3, nth + 1):
        if nums[-2] < sys.maxint - nums[-1]:
            nums.append(nums[-1] + nums[-2])
        else:
            raise OverflowError("Fibonacchi number will exceed max integer value, {0}. \
 Please decrease 'n', {1}.".format(sys.maxint, nth))
    return nums

def is_prime(num):
    """
    Check if the given number is prime number.
    :param num: input number
    :return: return True if num is prime. Otherwise, False.
    """
    if num in [0, 1]:
        return False
    elif num == 2:
        return True

    # even numbers are not prime number. eliminate them first.
    if num%2 == 0:
        return False

    # check if num can be divided by odd number greater than equals 3 up to
    # sqrt(num) + 1.
    for i in xrange(3, int(math.sqrt(num)) + 1, 2):
        if num%i == 0:
            return False
    return True

def fizz_buzz(nth):
    """
    Play Fizz buzz with a bit tweaked rule as below:
        generating the first n Fibonacci numbers F(n), printing ...
        - ... "Buzz" when F(n) is divisible by 3.
        - ... "Fizz" when F(n) is divisible by 5.
        - ... "FizzBuzz" when F(n) is divisible by both 3 and 5.
               (this rule is added according to general fizz buzz game.)
        - ... "BuzzFizz" when F(n) is prime.
        - ... the value F(n) otherwise.
    :param nth: nth parameter for Fibonacchi number
    """

    nums = []
    try:
        nums = fib(nth)
    except OverflowError as err:
        print(err)
        sys.exit()

    results = []
    for nth in xrange(0, len(nums)):
        if nums[nth] in [0, 1]:
            results.append((nums[nth]))
        elif nums[nth]%3 == 0 and nums[nth]%5 == 0:
            results.append("FizzBuzz")
        elif nums[nth]%3 == 0:
            results.append("Buzz")
        elif nums[nth]%5 == 0:
            results.append("Fizz")
        elif is_prime(nums[nth]):
            results.append("BuzzFizz")
        else:
            results.append((nums[nth]))

    return results

if __name__ == "__main__":
    if len(sys.argv) <= 0:
        sys.exit("Please specify the number for Fibonachii. e.g. application.py 10")
    print(*fizz_buzz(int(sys.argv[1])), sep=", ")

