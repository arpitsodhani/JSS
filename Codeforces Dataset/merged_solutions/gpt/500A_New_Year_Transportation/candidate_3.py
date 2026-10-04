# CLAUSE: parse_transport_plan
import sys

def parse_transport_plan():
    values = sys.stdin.buffer.read().split()
    n = int(values[0])
    t = int(values[1])
    jumps = tuple(int(x) for x in values[2:])
    return n, t, jumps

# CLAUSE: model_forward_reachability
def build_stepper(jumps):
    def step(cell):
        return cell + jumps[cell - 1]
    return step

# CLAUSE: advance_current_cell
def reaches_target(n, target, jumps):
    step = build_stepper(jumps)
    cell = 1
    while cell < target:

# CLAUSE: detect_target_arrival
        cell = step(cell)
        if cell == target:
            return True

# CLAUSE: enforce_monotone_bounds
        if cell > target or cell >= n:
            break

# CLAUSE: decide_reachability_output
    return cell == target

n, target, jumps = parse_transport_plan()
answer = reaches_target(n, target, jumps)
print("YES" if answer else "NO")
