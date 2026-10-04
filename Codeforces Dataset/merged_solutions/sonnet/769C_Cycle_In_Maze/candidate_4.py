# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.read().split()
    if not raw:
        return

    n, m, k = int(raw[0]), int(raw[1]), int(raw[2])
    field = raw[3:3 + n]
    total = n * m

    start = 0
    for r in range(n):
        for c, value in enumerate(field[r]):
            if value == "X":
                start = r * m + c

    if k % 2 == 1:
        print("IMPOSSIBLE")
        return

    steps = [("D", m), ("L", -1), ("R", 1), ("U", -m)]
    dist = [-1] * total
    dist[start] = 0
    q = deque([start])

    while q:
        pos = q.popleft()
        r, c = divmod(pos, m)
        for _, delta in steps:
            nxt = pos + delta
            nr, nc = divmod(nxt, m)
            if abs(nr - r) + abs(nc - c) != 1:
                continue
            if 0 <= nr < n and 0 <= nc < m and field[nr][nc] != "*" and dist[nxt] == -1:
                dist[nxt] = dist[pos] + 1
                q.append(nxt)

    pos = start
    out = []

    for used in range(k):
        r, c = divmod(pos, m)
        remaining = k - used - 1
        moved = False
        for ch, delta in steps:
            nxt = pos + delta
            nr, nc = divmod(nxt, m)
            if abs(nr - r) + abs(nc - c) != 1:
                continue
            if 0 <= nr < n and 0 <= nc < m and field[nr][nc] != "*":
                d = dist[nxt]
                if d != -1 and d <= remaining and (remaining - d) % 2 == 0:
                    out.append(ch)
                    pos = nxt
                    moved = True
                    break
        if not moved:
            print("IMPOSSIBLE")
            return

    print("".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
