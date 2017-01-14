# Uses python3
import sys
import unittest


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclid(a, b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(gcd_naive(18, 35), 1)
        self.assertEqual(gcd_naive(28851538, 1183019), 17657)

    def test_fast(self):
        self.assertEqual(gcd_euclid(18, 35), 1)
        self.assertEqual(gcd_euclid(28851538, 1183019), 17657)


if __name__ == '__main__':
    # unittest.main()

    # while(True):
    # 	a = random.randint(1, 10000)
    # 	b = random.randint(2, 10000)

    # 	res1 = gcd_naive(a, b)
    # 	res2 = gcd_euclid(a, b)
    # 	if (res1 != res2):
    # 		print('Wrond answer: {} {}'.format(res1, res2))
    # 		break
    # 	else:
    # 		print('OK: {} {}'.format(res1, res2))

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b))
