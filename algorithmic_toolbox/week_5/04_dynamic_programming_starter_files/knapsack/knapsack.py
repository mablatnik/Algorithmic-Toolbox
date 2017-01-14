# Uses python3
import sys


def optimal_weight(W, w):
    items = [0]
    for item in w:
        if item <= W:
            items.append(item)

    item_length = len(items)
    capacity = W + 1

    weights = [[0 for _ in range(item_length)] for _ in range(capacity)]

    for j in range(1, item_length):
        for i in range(1, capacity):
            previous = weights[i][j - 1]
            current = items[j] + weights[i - items[j]][j - 1]
            if current > i:
                weights[i][j] = previous
            else:
                weights[i][j] = max(previous, current)

    return weights[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
