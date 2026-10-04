# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    cards = data[2:2 + n]
    queries = data[2 + n:2 + n + q]

    seen = set()
    active = []
    for color in cards:
        if color not in seen:
            seen.add(color)
            active.append(color)

    result = []
    for target in queries:
        position = 1
        while active[position - 1] != target:
            position += 1
        result.append(str(position))
        if position != 1:
            active = [target] + active[:position - 1] + active[position:]

    sys.stdout.write(" ".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
