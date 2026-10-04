# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.80]
main()


