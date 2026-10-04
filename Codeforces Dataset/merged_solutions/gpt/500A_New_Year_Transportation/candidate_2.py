# CLAUSE: parse_transport_plan
import sys

def parse_transport_plan():
    first, second, *rest = map(int, sys.stdin.buffer.read().split())
    return first, second, rest

# CLAUSE: model_forward_reachability
def portal_destination(cell, jump_table):
    return cell + jump_table[cell - 1]

# CLAUSE: advance_current_cell
def can_arrive(n, target, jump_table):
    cell = 1
    reachable = False
    running = True
    while running:

# CLAUSE: detect_target_arrival
        if cell == target:
            reachable = True
            running = False

# CLAUSE: enforce_monotone_bounds
        elif cell > target or cell == n:
            running = False
        else:
            cell = portal_destination(cell, jump_table)

# CLAUSE: decide_reachability_output
    return reachable

n, target, jump_table = parse_transport_plan()
sys.stdout.write("YES\n" if can_arrive(n, target, jump_table) else "NO\n")
