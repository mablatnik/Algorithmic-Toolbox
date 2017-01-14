# Uses python3
import sys
import unittest


def get_change_specific(value):
    p, n, d = 1, 5, 10
    count = 0
    while value > 0:
        if value >= d:
            count += value // d
            value %= d
        elif value >= n:
            count += value // n
            value %= n
        else:
            count += value // p
            break
    return count


def get_change_abstract(value, *coins):
    count = 0
    i = 0
    while value > 0:
        count += value // coins[i]
        value %= coins[i]
        i += 1
    return count


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(get_change_specific(2), 2)
        self.assertEqual(get_change_specific(28), 6)

    def test_naive(self):
        self.assertEqual(get_change_abstract(2, 10, 5, 1), 2)
        self.assertEqual(get_change_abstract(28, 10, 5, 1), 6)


if __name__ == '__main__':
    # unittest.main()

    value = int(sys.stdin.read())
    print(get_change_specific(value))
