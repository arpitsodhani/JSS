# CLAUSE: parse_corridor_weights
import sys
from itertools import accumulate

stream = list(map(int, sys.stdin.buffer.read().split()))
n = stream[0]
a1_start = 1
a2_start = a1_start + n - 1
b_start = a2_start + n - 1

top_waits = stream[a1_start:a2_start]
bottom_waits = stream[a2_start:b_start]
vertical_waits = stream[b_start:b_start + n]

# CLAUSE: compute_row_prefix_costs
top_to_column = [0, *accumulate(top_waits)]
bottom_to_column = [0, *accumulate(bottom_waits)]
bottom_end_cost = bottom_to_column[n - 1]

# CLAUSE: evaluate_crossing_column_cost
def route_value(column_index):
    right_part_bottom = bottom_end_cost - bottom_to_column[column_index]
    left_part_top = top_to_column[column_index]
    return right_part_bottom + vertical_waits[column_index] + left_part_top

# CLAUSE: select_minimal_one_way_route
best_single_trip = route_value(0)
for column_index in range(n):
    value = route_value(column_index)
    if value < best_single_trip:
        best_single_trip = value

# CLAUSE: double_symmetric_trip_cost
sys.stdout.write(str(2 * best_single_trip))
