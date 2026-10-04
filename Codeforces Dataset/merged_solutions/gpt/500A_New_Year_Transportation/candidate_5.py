# CLAUSE: parse_transport_plan
import sys

def parse_transport_plan():
    numbers = [int(part) for part in sys.stdin.buffer.read().split()]
    board_size = numbers[0]
    target_cell = numbers[1]
    jump_by_cell = {cell: jump for cell, jump in enumerate(numbers[2:], start=1)}
    return board_size, target_cell, jump_by_cell

# CLAUSE: model_forward_reachability
def forward_neighbor(cell, jump_by_cell):
    return cell + jump_by_cell[cell]

# CLAUSE: advance_current_cell
def simulate(board_size, target_cell, jump_by_cell):
    cell = 1
    status = False
    while cell <= target_cell and cell < board_size:

# CLAUSE: detect_target_arrival
        if cell == target_cell:
            status = True
            break
        cell = forward_neighbor(cell, jump_by_cell)

# CLAUSE: enforce_monotone_bounds
        if cell > target_cell:
            break

# CLAUSE: decide_reachability_output
    return status or cell == target_cell

board_size, target_cell, jump_by_cell = parse_transport_plan()
print("YES" if simulate(board_size, target_cell, jump_by_cell) else "NO")
