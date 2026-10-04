# CLAUSE: parse_corridor_weights
from sys import stdin, stdout

tokens = [int(x) for x in stdin.buffer.read().split()]
n = tokens[0]
p = 1
upper = tokens[p:p + n - 1]
p += n - 1
lower = tokens[p:p + n - 1]
p += n - 1
middle = tokens[p:p + n]

# CLAUSE: compute_row_prefix_costs
upper_prefix = [0]
for value in upper:
    upper_prefix.append(upper_prefix[-1] + value)

lower_suffix = [0] * n
running = 0
for idx in range(n - 2, -1, -1):
    running += lower[idx]
    lower_suffix[idx] = running

# CLAUSE: evaluate_crossing_column_cost
def crossing_costs():
    for idx, vertical_cost in enumerate(middle):
        yield lower_suffix[idx] + vertical_cost + upper_prefix[idx]

# CLAUSE: select_minimal_one_way_route
best_cost = min(crossing_costs())

# CLAUSE: double_symmetric_trip_cost
stdout.write(f"{best_cost * 2}\n")
