# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.buffer.read().split()
    if not parts:
        return
    n = int(parts[0])
    x_bytes = parts[1]
    b_bytes = parts[2]
    answer = int(parts[4]) if len(parts) > 4 else 0
    index = 0
    while index < n:
        xb = x_bytes[index] & 1
        bb = b_bytes[index] & 1
        answer ^= xb ^ (bb ^ 1)
        index += 1
    sys.stdout.write(str(answer))

# CLAUSE: finish_program
main()
