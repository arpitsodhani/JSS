# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def classify(x, y):
    return ((x // 2) % 2) * 2 + ((y // 2) % 2)

def main():
    values = sys.stdin.read().split()
    if len(values) == 0:
        return

    n = int(values[0])
    buckets = [0 for _ in range(4)]
    pairs = [(int(values[i]), int(values[i + 1])) for i in range(1, len(values), 2)]

    for x, y in pairs:
        buckets[classify(x, y)] += 1

    answer = n * (n - 1) * (n - 2) // 6
    excluded = 0
    combinations = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
    for a, b, c in combinations:
        excluded += buckets[a] * buckets[b] * buckets[c]

    sys.stdout.write(str(answer - excluded) + "\n")

# CLAUSE: finish_program
main()
