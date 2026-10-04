# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 1.00]
def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    cells = b"".join(data[3:])

    pref = [[0] * m for _ in range(n + 1)]
    for i in range(n):
        base = i * m
        prev = pref[i]
        cur = pref[i + 1]
        for j in range(m):
            cur[j] = prev[j] + cells[base + j] - 48

    ans = 0
    for top in range(n):
        for bottom in range(top, n):
            total = 0
            seen = {0: 1}
            low = pref[top]
            high = pref[bottom + 1]
            for col in range(m):
                total += high[col] - low[col]
                ans += seen.get(total - k, 0)
                seen[total] = seen.get(total, 0) + 1
    sys.stdout.write(str(ans))


# Clause finish_program [Confidence: 0.80]
solve()


