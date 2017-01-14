# Uses python3
import sys
import unittest


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(get_fibonacci_last_digit_naive(3), 2)
        self.assertEqual(get_fibonacci_last_digit_naive(331), 9)
        self.assertEqual(get_fibonacci_last_digit_naive(327305), 5)

    def test_fast(self):
        self.assertEqual(get_fibonacci_last_digit_fast(3), 2)
        self.assertEqual(get_fibonacci_last_digit_fast(331), 9)
        self.assertEqual(get_fibonacci_last_digit_fast(327305), 5)


if __name__ == '__main__':
    # unittest.main()
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(n))
