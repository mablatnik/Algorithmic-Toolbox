def max_value_loot(value_p_w, knapsack):
    max_value = 0

    for i in value_p_w:
        if i[1] <= knapsack:
            max_value += round((i[0] * i[1]), 3)
            knapsack -= i[1]
        else:
            max_value += round((i[0] * i[1] * knapsack) / i[1], 3)
            knapsack = 0

    return max_value


items, knapsack = [int(i) for i in input().split()]

if 1 <= items <= 10 ** 3 and 0 <= knapsack <= 2 * (10 ** 6):
    weights = []
    values = []
    value_p_w = {}
    # value_per_unit_weight = []
    for i in range(items):
        value, weight = list(map(int, input().split()))
        if 0 <= value <= 2 * (10 ** 6) and 0 < weight <= 2 * (10 ** 6):
            # value_per_unit_weight.append(value / weight)
            weights.append(weight)
            values.append(value)

    for i in range(len(weights)):
        value_p_w[values[i] / weights[i]] = weights[i]

    value_p_w = sorted(value_p_w.items(), reverse=True)
    #print(value_p_w)

    print(max_value_loot(value_p_w, knapsack))

