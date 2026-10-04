# CLAUSE: setup_environment
import sys

input = sys.stdin.readline

# CLAUSE: solve_logic
def solve():
    n = int(input())
    total = n * n + 1
    buckets = [[] for _ in range(n + 1)]
    row = 0
    while row < n:
        first = row * (n + 1) + 1
        if first > total:
            break
        query = tuple(range(first, min(total, first + n) + 1))
        print("?", len(query), *query, flush=True)
        response = list(map(int, input().split()))
        visible = response[1:response[0] + 1]
        if len(visible) >= n + 1:
            print("!", *visible[:n + 1], flush=True)
            return
        visible_lookup = set(visible)
        for offset, position in enumerate(query):
            if position not in visible_lookup:
                buckets[offset].append(position)
        row += 1
    for bucket in buckets:
        if len(bucket) >= n + 1:
            print("!", *bucket[:n + 1], flush=True)
            return
    fallback = [i for i in range(1, n + 2)]
    print("!", *fallback, flush=True)

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
