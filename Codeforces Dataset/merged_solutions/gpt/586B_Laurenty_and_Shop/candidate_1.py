# CLAUSE: parse_corridor_weights
import sys

def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    first = values[1:n]
    second = values[n:2 * n - 1]
    avenue = values[2 * n - 1:3 * n - 1]
    return n, first, second, avenue

# CLAUSE: compute_row_prefix_costs
def build_prefix(row):
    pref = [0]
    for cost in row:
        pref.append(pref[-1] + cost)
    return pref

# CLAUSE: evaluate_crossing_column_cost
def cost_at_column(j, n, top_prefix, bottom_prefix, vertical):
    bottom_cost = bottom_prefix[n - 1] - bottom_prefix[j]
    top_cost = top_prefix[j]
    return bottom_cost + vertical[j] + top_cost

# CLAUSE: select_minimal_one_way_route
def best_one_way(n, top, bottom, vertical):
    top_prefix = build_prefix(top)
    bottom_prefix = build_prefix(bottom)
    best = None
    for j in range(n):
        current = cost_at_column(j, n, top_prefix, bottom_prefix, vertical)
        if best is None or current < best:
            best = current
    return best

# CLAUSE: double_symmetric_trip_cost
def main():
    n, top, bottom, vertical = read_input()
    print(best_one_way(n, top, bottom, vertical) * 2)

main()
