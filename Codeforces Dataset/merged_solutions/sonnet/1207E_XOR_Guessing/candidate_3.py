# CLAUSE: setup_environment
import sys

readline = sys.stdin.readline

def send(values):
    print("?", *values, flush=True)
    reply = int(readline())
    if reply == -1:
        sys.exit(0)
    return reply

# CLAUSE: solve_logic
small_values = [number for number in range(1, 101)]
large_values = [number * 128 for number in range(1, 101)]

low_part_mask = 127
high_part_mask = 16256

left = send(small_values)
right = send(large_values)
hidden = (left & high_part_mask) + (right & low_part_mask)

# CLAUSE: finish_program
print("!", hidden, flush=True)
