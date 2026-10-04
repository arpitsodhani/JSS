# CLAUSE: setup_environment
import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if len(data) == 0:
        return
    n = int(data[0])
    arr = [int(data[i]) for i in range(1, n + 1)]

# CLAUSE: solve_logic
    ranked_positions = sorted(range(n), key=lambda pos: (arr[pos], pos))
    where = [0] * n
    rank = [0] * n

    for r in range(n):
        p = ranked_positions[r]
        rank[p] = r
        where[r] = p

    work = deque(r for r in range(n - 1) if where[r] > where[r + 1])
    operations = []

    def refresh(center):
        start = max(0, center - 1)
        end = min(n - 2, center + 1)
        for r in range(start, end + 1):
            if where[r] > where[r + 1]:
                work.append(r)

    while work:
        r = work.popleft()
        if r >= n - 1 or where[r] < where[r + 1]:
            continue

        i = where[r]
        j = where[r + 1]
        left = min(i, j)
        right = max(i, j)
        operations.append((left + 1, right + 1))

        rank[i], rank[j] = rank[j], rank[i]
        where[r], where[r + 1] = where[r + 1], where[r]

        refresh(r)

# CLAUSE: finish_program
    output = [str(len(operations))]
    output.extend(f"{left} {right}" for left, right in operations)
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
