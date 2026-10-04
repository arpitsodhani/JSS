# Clause setup_environment [Confidence: 0.20]
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))


# Clause solve_logic [Confidence: 1.00]
def solve():
    n = int(sys.stdin.readline())
    total = n * n + 1
    queried = []
    for row in range(n):
        left = row * (n + 1) + 1
        right = min(left + n, total)
        if left > total:
            break
        group = list(range(left, right + 1))
        print("?", len(group), *group, flush=True)
        reply = readints()
        count = reply[0]
        visible = reply[1:count + 1]
        if len(visible) >= n + 1:
            print("!", *visible[:n + 1], flush=True)
            return
        queried.append((group, set(visible)))
    columns = [[] for _ in range(n + 1)]
    for group, seen in queried:
        for index, value in enumerate(group):
            if value not in seen:
                columns[index].append(value)
    for column in columns:
        if len(column) >= n + 1:
            print("!", *column[:n + 1], flush=True)
            return
    print("!", *range(1, n + 2), flush=True)


# Clause finish_program [Confidence: 0.60]
solve()


