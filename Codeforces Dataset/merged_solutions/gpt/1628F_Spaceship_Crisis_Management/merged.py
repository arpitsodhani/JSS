# CLAUSE: setup_environment
import sys
from math import gcd
from collections import deque

# CLAUSE: solve_logic
def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def dot(ax, ay, bx, by):
    return ax * bx + ay * by

def norm_dir(dx, dy):
    g = gcd(abs(dx), abs(dy))
    return dx // g, dy // g

def le_frac(a_num, a_den, b_num, b_den):
    return a_num * b_den <= b_num * a_den

def lt_frac(a_num, a_den, b_num, b_den):
    return a_num * b_den < b_num * a_den

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it)

    segs = []
    pts = [(0, 0)]
    mate = [-1]

    for _ in range(n):
        ax = next(it)
        ay = next(it)
        bx = next(it)
        by = next(it)
        i = len(pts)
        pts.append((ax, ay))
        pts.append((bx, by))
        mate.extend([i + 1, i])
        segs.append((ax, ay, bx, by, i, i + 1))

    q = next(it)
    queries = [(next(it), next(it)) for _ in range(q)]

    ans = []

    for sx, sy in queries:
        dirs = set()
        for px, py in pts:
            dx = sx - px
            dy = sy - py
            if dx or dy:
                dirs.add(norm_dir(dx, dy))

        ok = False

        for dx, dy in dirs:
            if ok:
                break

            vis = [False] * len(pts)
            que = deque([0])
            vis[0] = True

            while que and not ok:
                pidx = que.popleft()
                px, py = pts[pidx]

                qx = sx - px
                qy = sy - py
                qt_num = dot(qx, qy, dx, dy)
                q_on = cross(qx, qy, dx, dy) == 0 and qt_num >= 0

                events = []

                for ax, ay, bx, by, ia, ib in segs:
                    vx = bx - ax
                    vy = by - ay
                    den = cross(dx, dy, vx, vy)
                    apx = ax - px
                    apy = ay - py

                    if den == 0:
                        if cross(apx, apy, dx, dy) != 0:
                            continue
                        ta = dot(ax - px, ay - py, dx, dy)
                        tb = dot(bx - px, by - py, dx, dy)
                        if ta > 0:
                            events.append((ta, 1, 1, ia, ib, False))
                        if tb > 0:
                            events.append((tb, 1, 1, ib, ia, False))
                        continue

                    tn = cross(apx, apy, vx, vy)
                    un = cross(apx, apy, dx, dy)
                    if den < 0:
                        den = -den
                        tn = -tn
                        un = -un

                    if tn <= 0 or un < 0 or un > den:
                        continue

                    hard = abs(cross(dx, dy, vx, vy)) >= abs(dot(dx, dy, vx, vy))
                    if un == 0:
                        events.append((tn, den, 1, ia, ib, hard))
                    elif un == den:
                        events.append((tn, den, 1, ib, ia, hard))
                    else:
                        events.append((tn, den, 0, -1, -1, hard))

                events.sort(key=lambda e: e[0] / e[1])

                blocked = False
                for tn, td, endpoint, aidx, bidx, hard in events:
                    if q_on and le_frac(qt_num, 1, tn, td):
                        ok = True
                        break

                    if endpoint and not hard:
                        if not vis[bidx]:
                            vis[bidx] = True
                            que.append(bidx)
                    else:
                        blocked = True
                        break

                if not ok and not blocked and q_on:
                    ok = True

        ans.append("YES" if ok else "NO")

    print("\n".join(ans))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
