# Uses python3
import sys
import unittest


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current


def fibonacci_sum_fast(n):
    new_n = (n + 2) % 60
    new_last = get_fibonacci_last_digit_fast(new_n)
    if new_last == 0:
        return 9
    else:
        return new_last - 1


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(fibonacci_sum_naive(3), 4)
        self.assertEqual(fibonacci_sum_naive(100), 5)

    def test_fast(self):
        self.assertEqual(fibonacci_sum_fast(3), 4)
        self.assertEqual(fibonacci_sum_fast(100), 5)


if __name__ == '__main__':
    # unittest.main()

    # while(True):
    #   a = random.randint(1, 100)

    #   res1 = fibonacci_sum_naive(a)
    #   res2 = fibonacci_sum_fast(a)
    #   if (res1 != res2):
    #     print('Generated: {}'.format(a))
    #     print('Wrond answer: {} {}'.format(res1, res2))
    #     break
    #   else:
    #     print('OK: {} {}'.format(res1, res2))

    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
