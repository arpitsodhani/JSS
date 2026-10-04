# CLAUSE: setup_environment
import sys

def main():
    n, pos, l, r = map(int, sys.stdin.buffer.read().split())

# CLAUSE: solve_logic
    if l == 1 and r == n:
        ans = 0
    elif l == 1:
        ans = abs(pos - r) + 1
    elif r == n:
        ans = abs(pos - l) + 1
    else:
        ans = min(abs(pos - l), abs(pos - r)) + (r - l) + 2

# CLAUSE: finish_program
    sys.stdout.write(str(ans))

main()
