# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def enough_rounds(distance, rounds):
    span = 1
    used = 0
    while span < distance and used < rounds:
        span += span
        used += 1
    return span >= distance

def program(n, k):
    if n == 1:
        return ["1" for _ in range(k)]
    distance = n - 1
    if not enough_rounds(distance, k):
        return ["-1"]
    rows = []
    covered = 1
    for _ in range(k):
        nxt = min(distance, covered + covered)
        values = []
        for index in range(n):
            d = n - index - 1
            if d <= covered:
                values.append(str(n))
            elif d <= nxt:
                values.append(str(n - d + covered))
            else:
                values.append(str(n - nxt + covered))
        rows.append(" ".join(values))
        covered = nxt
    return rows

# CLAUSE: finish_program
def main():
    items = sys.stdin.buffer.read().split()
    if len(items) >= 2:
        result = program(int(items[0]), int(items[1]))
        sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
