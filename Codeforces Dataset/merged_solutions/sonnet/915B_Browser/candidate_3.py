# CLAUSE: setup_environment
import sys

def distance_to_close(n, pos, l, r):
    left_needed = l > 1
    right_needed = r < n

# CLAUSE: solve_logic
    if not left_needed and not right_needed:
        return 0
    if left_needed and not right_needed:
        return abs(pos - l) + 1
    if right_needed and not left_needed:
        return abs(pos - r) + 1
    go_left_first = abs(pos - l) + (r - l)
    go_right_first = abs(pos - r) + (r - l)
    return min(go_left_first, go_right_first) + 2

# CLAUSE: finish_program
data = list(map(int, sys.stdin.buffer.read().split()))
print(distance_to_close(*data))
