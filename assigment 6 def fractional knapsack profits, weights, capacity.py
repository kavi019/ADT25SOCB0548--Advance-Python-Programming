def fractional_knapsack(profits, weights, capacity):
    n = len(profits)
    items = [(profits[i], weights[i], profits[i] / weights[i]) for i in range(n)]
    items.sort(key=lambda item: item[2], reverse=True)
    total_profit = 0.0
    remaining = capacity
    chosen = []
    for profit, weight, ratio in items:
        if remaining <= 0:
            break
        if weight <= remaining:
            total_profit += profit
            remaining -= weight
            chosen.append((profit, weight, 1.0))
        else:
            fraction = remaining / weight
            total_profit += profit * fraction
            chosen.append((profit, weight, fraction))
            remaining = 0
    return total_profit, chosen

def knapsack_brute_force(weights, values, capacity, n=None):
    if n is None:
        n = len(weights)
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack_brute_force(weights, values, capacity, n - 1)
    include = values[n - 1] + knapsack_brute_force(weights, values, capacity - weights[n - 1], n - 1)
    exclude = knapsack_brute_force(weights, values, capacity, n - 1)
    return max(include, exclude)

def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}
    def helper(i, remaining_capacity):
        if i == 0 or remaining_capacity == 0:
            return 0
        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]
        if weights[i - 1] > remaining_capacity:
            result = helper(i - 1, remaining_capacity)
        else:
            include = values[i - 1] + helper(i - 1, remaining_capacity - weights[i - 1])
            exclude = helper(i - 1, remaining_capacity)
            result = max(include, exclude)
        memo[(i, remaining_capacity)] = result
        return result
    return helper(n, capacity)

def build_knapsack_table(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                skip = dp[i - 1][w]
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                dp[i][w] = max(skip, take)
    return dp

def reconstruct_selected_items(dp, weights, values, capacity):
    n = len(weights)
    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()
    return selected

def knapsack_bottom_up(weights, values, capacity):
    dp = build_knapsack_table(weights, values, capacity)
    n = len(weights)
    max_value = dp[n][capacity]
    selected = reconstruct_selected_items(dp, weights, values, capacity)
    return max_value, selected, dp

if __name__ == "__main__":
    f_profits = [25, 24, 15]
    f_weights = [18, 15, 10]
    f_capacity = 20
    total_p, chosen_items = fractional_knapsack(f_profits, f_weights, f_capacity)
    print(total_p)
    for p, w, frac in chosen_items:
        print(p, w, frac)

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print(knapsack_brute_force(weights, values, capacity))
    print(knapsack_top_down(weights, values, capacity))
    max_val, selected, dp_grid = knapsack_bottom_up(weights, values, capacity)
    print(max_val)
    print(selected)