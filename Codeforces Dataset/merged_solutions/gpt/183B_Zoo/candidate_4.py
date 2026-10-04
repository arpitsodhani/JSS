# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from math import gcd
    from collections import defaultdict

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    pts = [(data[i], data[i + 1]) for i in range(2, 2 + 2 * m, 2)]

    candidates = set()

    for i in range(m):
        x1, y1 = pts[i]
        for j in range(i + 1, m):
            x2, y2 = pts[j]
            den = y2 - y1
            if den == 0:
                continue
            num = x1 * y2 - x2 * y1
            if num % den == 0:
                k = num // den
                if 1 <= k <= n:
                    candidates.add(k)

    ans = n

    for k in candidates:
        cnt = defaultdict(int)
        best = 1
        for x, y in pts:
            dx = x - k
            g = gcd(abs(dx), y)
            key = (dx // g, y // g)
            cnt[key] += 1
            if cnt[key] > best:
                best = cnt[key]
        ans += best - 1

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
