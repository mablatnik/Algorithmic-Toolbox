# Uses python3
import sys
import random

def quick_sort_partition3(a, left, right):
    if left < right:
        pivot = random.randint(left, right-1)
        pivot_value = a[pivot]
        p_l1 = p_l2 = left
        p_e = right
        while p_l2 < p_e:
            if a[p_l2] < pivot_value:
                a[p_l2], a[p_l1] = a[p_l1], a[p_l2]
                p_l1 += 1
                p_l2 += 1
            elif a[p_l2] == pivot_value:
                p_l2 += 1
            else:
                p_e -= 1
                a[p_l2], a[p_e] = a[p_e], a[p_l2]
        quick_sort_partition3(a, left, p_l1)
        quick_sort_partition3(a, p_e, right)

def partition2(a, left, right):
    pivot = random.randint(left, right)
    a[right], a[pivot] = a[pivot], a[right]
    pivot_value = a[right]
    pIndex = left;
    for i in range(left, right):
        if a[i] <= pivot_value:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[right], a[pIndex] = a[pIndex], a[right]
    return pIndex


def randomized_quick_sort(a, left, right):
    if left < right:
        pIndex = partition3(a, left, right)
        randomized_quick_sort(a, left, pIndex - 1);
        randomized_quick_sort(a, pIndex + 1, right);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort_partition3(a, 0, n)
    for x in a:
        print(x, end=' ')
