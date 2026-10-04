# CLAUSE: setup_environment
import sys

def ask(items):
    print("?", len(items), *items, flush=True)
    data = list(map(int, sys.stdin.readline().split()))
    return data[1:data[0] + 1]

# CLAUSE: solve_logic
def solve():
    n = int(sys.stdin.readline())
    limit = n * n + 1
    rows = []
    starts = range(1, limit + 1, n + 1)
    for start in starts:
        if len(rows) == n:
            break
        row = [x for x in range(start, min(limit, start + n) + 1)]
        visible = ask(row)
        if len(visible) >= n + 1:
            print("!", *visible[:n + 1], flush=True)
            return
        rows.append((row, visible))
    hidden_by_offset = [[] for _ in range(n + 1)]
    for row, visible in rows:
        visible = set(visible)
        for offset in range(len(row)):
            value = row[offset]
            if value not in visible:
                hidden_by_offset[offset].append(value)
    answer = None
    for values in hidden_by_offset:
        if len(values) >= n + 1:
            answer = values[:n + 1]
            break
    if answer is None:
        answer = list(range(1, n + 2))
    print("!", *answer, flush=True)

# CLAUSE: finish_program
solve()
