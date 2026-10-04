# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    camels = []
    at = 1
    for _ in range(n):
        camels.append((values[at], values[at + 1]))
        at += 2

    seen = set(camels)
    answer = "NO"
    for x, d in camels:
        if d and (x + d, -d) in seen:
            answer = "YES"
            break

    sys.stdout.write(answer)

# CLAUSE: finish_program
main()
