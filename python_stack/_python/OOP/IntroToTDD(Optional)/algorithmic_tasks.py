import unittest

def reverseList(arr):
    """Reverses the values in the list in-place."""
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr

def isPalindrome(word):
    """Checks if a given string is a palindrome."""
    return word == word[::-1]

def coins(amount):
    """Calculates the minimum number of coins for the given amount."""
    res = []
    # Quarters, Dimes, Nickels, Pennies
    for coin in [25, 10, 5, 1]:
        count = amount // coin
        res.append(count)
        amount %= coin
    return res

def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class TestAlgorithmicTasks(unittest.TestCase):

    def test_reverseList(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
        self.assertEqual(reverseList([1, 2]), [2, 1])
        self.assertEqual(reverseList([1]), [1])
        self.assertEqual(reverseList([]), [])

    def test_isPalindrome(self):
        self.assertTrue(isPalindrome("racecar"))
        self.assertFalse(isPalindrome("rabcr"))
        self.assertTrue(isPalindrome("madam"))
        self.assertTrue(isPalindrome("a"))
        self.assertTrue(isPalindrome(""))
        self.assertFalse(isPalindrome("hello"))

    def test_coins(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])
        self.assertEqual(coins(41), [1, 1, 1, 1])
        self.assertEqual(coins(10), [0, 1, 0, 0])
        self.assertEqual(coins(5), [0, 0, 1, 0])
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(4), 24)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(6), 8)
        
if __name__ == '__main__':
    unittest.main()