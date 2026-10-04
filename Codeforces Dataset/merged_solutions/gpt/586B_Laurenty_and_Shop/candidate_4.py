# CLAUSE: parse_corridor_weights
import sys

raw = sys.stdin.buffer.read().split()
n = int(raw[0])
numbers = tuple(map(int, raw[1:]))
row_top = numbers[:n - 1]
row_bottom = numbers[n - 1:2 * n - 2]
row_vertical = numbers[2 * n - 2:2 * n - 2 + n]

# CLAUSE: compute_row_prefix_costs
top_prefix = [0] * n
for col, edge_cost in enumerate(row_top, start=1):
    top_prefix[col] = top_prefix[col - 1] + edge_cost

bottom_prefix = [0] * n
for col, edge_cost in enumerate(row_bottom, start=1):
    bottom_prefix[col] = bottom_prefix[col - 1] + edge_cost

# CLAUSE: evaluate_crossing_column_cost
all_costs = []
for col in range(n):
    from_home_to_crossing = bottom_prefix[-1] - bottom_prefix[col]
    crossing = row_vertical[col]
    from_crossing_to_shop = top_prefix[col]
    all_costs.append(from_home_to_crossing + crossing + from_crossing_to_shop)

# CLAUSE: select_minimal_one_way_route
answer_one_way = all_costs[0]
for candidate in all_costs[1:]:
    answer_one_way = min(answer_one_way, candidate)

# CLAUSE: double_symmetric_trip_cost
print(answer_one_way + answer_one_way)
