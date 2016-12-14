#Uses python3

import sys

def largest_number(a):
    res = ""
    while len(a) > 0:
    	max_digit = 1e-10
	    for x in a:
	    	

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
