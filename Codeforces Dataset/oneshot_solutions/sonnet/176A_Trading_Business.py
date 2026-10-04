import sys

input_data = sys.stdin.read().strip().split('\n')
idx = 0

n, m, k = map(int, input_data[idx].split())
idx += 1

planets = []
for i in range(n):
    name = input_data[idx]
    idx += 1
    items = []
    for j in range(m):
        a, b, c = map(int, input_data[idx].split())
        idx += 1
        items.append((a, b, c))
    planets.append(items)

max_profit = 0

# Try all pairs of planets
for buy_planet in range(n):
    for sell_planet in range(n):
        if buy_planet == sell_planet:
            continue
        
        # Calculate profit for each item type
        profits = []
        for item_type in range(m):
            a = planets[buy_planet][item_type][0]  # buy cost
            b = planets[sell_planet][item_type][1]  # sell cost
            c = planets[buy_planet][item_type][2]  # count available
            profit_per_item = b - a
            if profit_per_item > 0 and c > 0:
                profits.append((profit_per_item, c))
        
        # Sort by profit in descending order
        profits.sort(reverse=True)
        
        # Greedily pick items
        total_profit = 0
        items_taken = 0
        for profit_per_item, count in profits:
            can_take = min(count, k - items_taken)
            total_profit += profit_per_item * can_take
            items_taken += can_take
            if items_taken >= k:
                break
        
        max_profit = max(max_profit, total_profit)

print(max_profit)
