import sys
from bisect import bisect_right

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        vals = sorted(set(a))
        m = len(vals)
        comp = {v: i for i, v in enumerate(vals)}
        pos = [[] for _ in range(m)]
        for i, x in enumerate(a):
            pos[comp[x]].append(i)

        best = 0
        for l in range(m):
            last = -1
            cur = 0
            for r in range(l, m):
                p = pos[r]
                j = bisect_right(p, last)
                if j == len(p):
                    break
                cur += len(p) - j
                last = p[-1]
                best = max(best, cur)

        ans.append(str(n - best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
