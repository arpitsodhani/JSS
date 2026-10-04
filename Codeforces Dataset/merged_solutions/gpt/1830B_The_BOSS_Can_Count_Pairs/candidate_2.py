# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n
        b = data[p:p + n]
        p += n
        groups = {}
        vals = []
        for x, y in zip(a, b):
            if x not in groups:
                groups[x] = defaultdict(int)
                vals.append(x)
            groups[x][y] += 1
        vals.sort()
        ans = 0
        for x in vals:
            gx = groups[x]
            limit = 2 * n // x
            for y in vals:
                if y < x:
                    continue
                if y > limit:
                    break
                s = x * y
                gy = groups[y]
                if x == y:
                    for u, cu in gx.items():
                        v = s - u
                        if v < u:
                            continue
                        cv = gx.get(v, 0)
                        if not cv:
                            continue
                        if u == v:
                            ans += cu * (cu - 1) // 2
                        else:
                            ans += cu * cv
                elif len(gx) <= len(gy):
                    for u, cu in gx.items():
                        ans += cu * gy.get(s - u, 0)
                else:
                    for v, cv in gy.items():
                        ans += cv * gx.get(s - v, 0)
        out.append(str(ans))
    print('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
