import sys
from bisect import bisect_right

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    T = next(it)
    out = []

    INF = 10**30

    for _ in range(T):
        n = next(it)
        m = next(it)
        q = next(it)

        a = [next(it) for _ in range(n)]
        d = [next(it) for _ in range(n)]
        l = [next(it) for _ in range(m)]
        times = [next(it) for _ in range(q)]

        tasks = sorted(zip(d, a))
        deadlines = []
        pref = []
        s = 0
        for dd, aa in tasks:
            s += aa
            deadlines.append(dd)
            pref.append(s)

        suf = [INF] * (n + 1)
        for i in range(n - 1, -1, -1):
            slack = deadlines[i] - pref[i]
            suf[i] = slack if slack < suf[i + 1] else suf[i + 1]

        ep = [0]
        s = 0
        for x in l:
            s += x
            ep.append(s)

        ans = []
        for t in times:
            idx = bisect_right(deadlines, t)
            done = pref[idx - 1] if idx else 0
            cap1 = t - done
            cap2 = suf[idx]
            cap = cap1 if cap1 < cap2 else cap2
            if cap < 0:
                ans.append("0")
            else:
                ans.append(str(bisect_right(ep, cap) - 1))

        out.append(" ".join(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
