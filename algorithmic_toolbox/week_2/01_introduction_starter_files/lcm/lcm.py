# Uses python3
import sys
import unittest


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd_euclid(a, b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend


def lcm_fast(a, b):
    return (a * b) // gcd_euclid(a, b)


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(lcm_naive(6, 8), 24)

    # self.assertEqual( lcm_naive(28851538, 1183019), 1933053046)

    def test_fast(self):
        self.assertEqual(lcm_fast(6, 8), 24)
        self.assertEqual(lcm_fast(28851538, 1183019), 1933053046)


if __name__ == '__main__':
    # unittest.main()

    # while(True):
    # 	a = random.randint(1, 1000)
    # 	b = random.randint(2, 1000)

    # 	res1 = lcm_naive(a, b)
    # 	res2 = lcm_fast(a, b)
    # 	if (res1 != res2):
    # 		print('Wrond answer: {} {}'.format(res1, res2))
    # 		break
    # 	else:
    # 		print('OK: {} {}'.format(res1, res2))

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
