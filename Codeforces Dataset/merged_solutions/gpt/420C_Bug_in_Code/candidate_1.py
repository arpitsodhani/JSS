# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, p = data[0], data[1]
    deg = [0] * (n + 1)
    edges = defaultdict(int)

    idx = 2
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        deg[a] += 1
        deg[b] += 1
        if a > b:
            a, b = b, a
        edges[(a, b)] += 1

    sorted_deg = sorted(deg[1:])
    ans = 0
    r = n - 1

    for l in range(n):
        while r > l and sorted_deg[l] + sorted_deg[r] >= p:
            r -= 1
        ans += n - max(r + 1, l + 1)

    for (a, b), c in edges.items():
        s = deg[a] + deg[b]
        if s >= p and s - c < p:
            ans -= 1

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
