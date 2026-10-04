# CLAUSE: parse_corridor_weights
import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
top_edges = data[1:1 + n - 1]
bottom_edges = data[1 + n - 1:1 + 2 * (n - 1)]
crossings = data[1 + 2 * (n - 1):]

# CLAUSE: compute_row_prefix_costs
top_left_cost = [0] * n
bottom_left_cost = [0] * n

for i in range(1, n):
    top_left_cost[i] = top_left_cost[i - 1] + top_edges[i - 1]
    bottom_left_cost[i] = bottom_left_cost[i - 1] + bottom_edges[i - 1]

bottom_total = bottom_left_cost[-1]

# CLAUSE: evaluate_crossing_column_cost
def one_way_through(column):
    return (bottom_total - bottom_left_cost[column]) + crossings[column] + top_left_cost[column]

# CLAUSE: select_minimal_one_way_route
minimum_route = one_way_through(0)
for column in range(1, n):
    route_cost = one_way_through(column)
    if route_cost < minimum_route:
        minimum_route = route_cost

# CLAUSE: double_symmetric_trip_cost
sys.stdout.write(str(minimum_route * 2))
