# CLAUSE: parse_transport_plan
import sys

def parse_transport_plan():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, t = data[0], data[1]
    jumps = [0] + data[2:]
    return n, t, jumps

# CLAUSE: model_forward_reachability
def next_cell(position, jumps):
    return position + jumps[position]

# CLAUSE: advance_current_cell
def follow_path(n, t, jumps):
    current = 1

# CLAUSE: detect_target_arrival
    while current != t:

# CLAUSE: enforce_monotone_bounds
        if current > t or current >= n:
            return False
        current = next_cell(current, jumps)

# CLAUSE: decide_reachability_output
    return True

n, t, jumps = parse_transport_plan()
print("YES" if follow_path(n, t, jumps) else "NO")
