# Uses python3
import sys, unittest, random

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current


def fib_period_length(n, m):
    period = []
    k = a = 0
    while(period[:k] != period[k:] or k<1):
        period.append(get_fibonacci(a) % m)
        a += 1
        k = len(period)//2
    return len(period)//2


def get_fibonacci_huge_fast(n, m):
    remainder = n % fib_period_length(n, m)
    return get_fibonacci(remainder) % m


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual( get_fibonacci_huge_naive(1, 239), 1)
        self.assertEqual( get_fibonacci_huge_naive(239, 1000), 161)

    def test_fast(self):
        self.assertEqual( get_fibonacci_huge_fast(1, 239), 1)
        self.assertEqual( get_fibonacci_huge_fast(239, 1000), 161)
        self.assertEqual( get_fibonacci_huge_fast(2816213588, 30524), 10249)


if __name__ == '__main__':
    unittest.main()

    # while(True):
    #   a = random.randint(1, 1000)
    #   b = random.randint(2, 100)

    #   res1 = get_fibonacci_huge_naive(a, b)
    #   res2 = get_fibonacci_huge_fast(a, b)
    #   if (res1 != res2):
    #       print('Wrond answer: {} {}'.format(res1, res2))
    #       break
    #   else:
    #       print('OK: {} {}'.format(res1, res2))

    # input = sys.stdin.read();
    # n, m = map(int, input.split())
    # print(get_fibonacci_huge_fast(n, m))

