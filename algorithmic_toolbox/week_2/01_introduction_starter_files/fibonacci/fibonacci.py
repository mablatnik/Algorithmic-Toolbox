# Uses python3


def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


n = int(input())
print(calc_fib(n))
