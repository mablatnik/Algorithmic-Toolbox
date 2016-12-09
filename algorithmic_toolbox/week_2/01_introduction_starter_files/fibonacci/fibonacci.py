# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    fib_1 = 0
    fib_2 = 1
    fib_currnent = 2

    i = 2
    while i <= n:
    	fib_currnent = fib_1 + fib_2
    	fib_1 = fib_2
    	fib_2 = fib_currnent
    	i += 1

    return fib_currnent


n = int(input())
print(calc_fib(n))
