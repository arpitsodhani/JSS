# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + 2 * n]
        idx += 2 * n
        m = 2 * n
        zeros = [i for i, x in enumerate(a) if x == 0]
        seen = [0] * (n + 1)
        stamp = 0

        def mex_interval(l, r):
            nonlocal stamp
            stamp += 1
            for i in range(l, r + 1):
                seen[a[i]] = stamp
            x = 0
            while x < n and seen[x] == stamp:
                x += 1
            return x

        def odd_center(c):
            l = r = c
            while l > 0 and r + 1 < m and (a[l - 1] == a[r + 1]):
                l -= 1
                r += 1
            return (l, r)
        ans = 1
        for z in zeros:
            l, r = odd_center(z)
            ans = max(ans, mex_interval(l, r))
        l, r = (zeros[0], zeros[1])
        x, y = (l, r)
        ok = True
        while x < y:
            if a[x] != a[y]:
                ok = False
                break
            x += 1
            y -= 1
        if ok:
            while l > 0 and r + 1 < m and (a[l - 1] == a[r + 1]):
                l -= 1
                r += 1
            ans = max(ans, mex_interval(l, r))
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
