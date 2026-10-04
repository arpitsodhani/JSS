# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    p, q, n = values[0], values[1], values[2]
    terms = values[3:]

    idx = 0
    while idx < n:
        if q == 0:
            sys.stdout.write("NO")
            return

        current = p // q
        if current != terms[idx]:
            sys.stdout.write("NO")
            return

        p %= q
        if idx == n - 1:
            sys.stdout.write("YES" if p == 0 else "NO")
            return

        if p == 0:
            sys.stdout.write("NO")
            return

        p, q = q, p
        idx += 1

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
