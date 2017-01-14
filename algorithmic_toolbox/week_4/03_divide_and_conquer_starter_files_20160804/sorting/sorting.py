# Uses python3
import sys
import random


def partition3(a, left, right):
    pivot_value = a[left]
    p_l = i = left
    p_e = right
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes


def partition2(a, left, right):
    pivot = random.randint(left, right)
    a[right], a[pivot] = a[pivot], a[right]
    pivot_value = a[right]
    pIndex = left
    for i in range(left, right):
        if a[i] <= pivot_value:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[right], a[pIndex] = a[pIndex], a[right]
    return pIndex


def randomized_quick_sort(a, left, right):
    if left >= right:
        return

    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    pIndex = partition3(a, left, right)
    randomized_quick_sort(a, left, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
