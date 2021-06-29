# Uses python3

import sys


def largest_number(a):
    res = ''

    nums = list(map(str, a))
    nums.sort(reverse=True)

    for x in nums:
        res += x

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
