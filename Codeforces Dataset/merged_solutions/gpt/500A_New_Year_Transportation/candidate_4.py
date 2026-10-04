# CLAUSE: parse_transport_plan
import sys

def parse_transport_plan():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(stream)
    target = next(stream)
    jumps = [next(stream) for _ in range(n - 1)]
    return n, target, jumps

# CLAUSE: model_forward_reachability
def move_once(cell, jumps):
    index = cell - 1
    return cell + jumps[index]

# CLAUSE: advance_current_cell
def trace_until_decided(n, target, jumps):
    cell = 1
    arrived = cell == target
    while not arrived and cell < target and cell < n:
        cell = move_once(cell, jumps)

# CLAUSE: detect_target_arrival
        arrived = cell == target

# CLAUSE: enforce_monotone_bounds
        if cell > target:
            break

# CLAUSE: decide_reachability_output
    return arrived

n, target, jumps = parse_transport_plan()
if trace_until_decided(n, target, jumps):
    print("YES")
else:
    print("NO")
