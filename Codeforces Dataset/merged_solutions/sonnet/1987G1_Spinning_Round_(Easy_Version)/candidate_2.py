# CLAUSE: setup_environment
import sys
from functools import lru_cache

sys.setrecursionlimit(300000)

def best_pair_sum(items):
    a = b = 0
    for v in items:
        if v > a:
            b = a
            a = v
        elif v > b:
            b = v
    return a + b

# CLAUSE: solve_logic
def solve_case(n, p):
    size = 1
    while size < n:
        size <<= 1
    seg = [0] * (2 * size)

    def better(x, y):
        if x == 0:
            return y
        if y == 0:
            return x
        if p[x - 1] > p[y - 1]:
            return x
        return y

    for i in range(n):
        seg[size + i] = i + 1
    for i in range(size - 1, 0, -1):
        seg[i] = better(seg[i << 1], seg[i << 1 | 1])

    def maximum_position(l, r):
        l += size - 1
        r += size - 1
        res = 0
        while l <= r:
            if l & 1:
                res = better(res, seg[l])
                l += 1
            if not (r & 1):
                res = better(res, seg[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def keep(states):
        unique = list(set(states))
        ans = []
        for st in unique:
            ok = True
            for ot in unique:
                if ot != st and ot[0] >= st[0] and ot[1] >= st[1] and ot[2] >= st[2] and ot[3] >= st[3]:
                    ok = False
                    break
            if ok:
                ans.append(st)
        return tuple(ans)

    @lru_cache(None)
    def dp(l, r, hl, hr):
        if l > r:
            return ((0, 0, 0, 0),)
        m = maximum_position(l, r)
        left = dp(l, m - 1, hl, 1)
        right = dp(m + 1, r, 1, hr)
        out = []
        for a in left:
            lh, ld, ml, dl = a
            for b in right:
                mr, dr, rh, rd = b
                if hl:
                    xh = max(lh, 1 + max(ml, mr))
                    xd = max(ld, dl, dr, best_pair_sum((1 + lh, ml, mr)))
                    out.append((xh, xd, rh, rd))
                if hr:
                    yh = max(rh, 1 + max(ml, mr))
                    yd = max(rd, dl, dr, best_pair_sum((ml, mr, 1 + rh)))
                    out.append((lh, ld, yh, yd))
        return keep(out)

    root = p.index(n) + 1
    left = dp(1, root - 1, 0, 1)
    right = dp(root + 1, n, 1, 0)
    ans = 0
    for a in left:
        for b in right:
            ans = max(ans, a[3], b[1], a[2] + b[0])
    return ans

# CLAUSE: finish_program
def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    at = 1
    res = []
    for _ in range(q):
        n = int(data[at])
        at += 1
        p = list(map(int, data[at:at + n]))
        at += n
        at += 1
        res.append(str(solve_case(n, p)))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
