# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def solve_case(n, k, a, b):
    mid = n // 2
    need = n - mid
    order = sorted(range(n), key=a.__getitem__)
    vals = [a[i] for i in order]
    pos = [0] * n
    for r, i in enumerate(order):
        pos[i] = r

    ans = 0
    for i, flag in enumerate(b):
        if flag:
            if pos[i] <= mid - 1:
                med = vals[mid]
            else:
                med = vals[mid - 1]
            cur = a[i] + k + med
            if cur > ans:
                ans = cur

    removed = -1
    for x, flag in zip(a, b):
        if flag == 0 and x > removed:
            removed = x

    if removed >= 0:
        ones = sorted(x for x, flag in zip(a, b) if flag)
        pref = [0]
        for x in ones:
            pref.append(pref[-1] + x)

        def ok(x):
            already = n - bisect_left(vals, x)
            if removed >= x:
                already -= 1
            lack = need - already
            if lack <= 0:
                return True
            p = bisect_left(ones, x)
            if p < lack:
                return False
            return lack * x - (pref[p] - pref[p - lack]) <= k

        lo, hi = 0, max(a) + k + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if ok(md):
                lo = md
            else:
                hi = md
        ans = max(ans, removed + lo)

    return ans

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    at = 1
    res = []
    for _ in range(t):
        n = data[at]
        k = data[at + 1]
        at += 2
        a = data[at:at + n]
        at += n
        b = data[at:at + n]
        at += n
        res.append(str(solve_case(n, k, a, b)))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
