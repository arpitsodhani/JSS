# Clause parse_transport_plan [Confidence: 0.80]
import sys

def parse_transport_plan():
    values = sys.stdin.buffer.read().split()
    n = int(values[0])
    t = int(values[1])
    jumps = tuple(int(x) for x in values[2:])
    return n, t, jumps


# Clause model_forward_reachability [Confidence: 0.80]
def forward_neighbor(cell, jump_by_cell):
    return cell + jump_by_cell[cell]


# Clause advance_current_cell [Confidence: 0.60]
def simulate(board_size, target_cell, jump_by_cell):
    cell = 1
    status = False
    while cell <= target_cell and cell < board_size:


# Clause detect_target_arrival [Confidence: 0.20]
        cell = step(cell)
        if cell == target:
            return True


# Clause enforce_monotone_bounds [Confidence: 0.40]
        if cell > target:
            break


# Clause decide_reachability_output [Confidence: 0.80]
    return status or cell == target_cell

board_size, target_cell, jump_by_cell = parse_transport_plan()
print("YES" if simulate(board_size, target_cell, jump_by_cell) else "NO")


