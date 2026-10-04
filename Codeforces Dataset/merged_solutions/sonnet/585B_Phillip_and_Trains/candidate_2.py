# CLAUSE: setup_environment
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    p = 0
    t = int(data[p])
    p += 1
    out = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = int(data[p])
        p += 2
        grid = []
        start = None
        for r in range(3):
            row = data[p]
            p += 1
            if "s" in row:
                start = (r, row.index("s"))
                row = row.replace("s", ".")
            grid.append(row + "." * 20)

        def unsafe(r, c, tm):
            c += 2 * tm
            return c < n and grid[r][c] != "."

        q = deque([(start[0], start[1], 0)])
        seen = {(start[0], start[1], 0)}
        good = False

        while q and not good:
            r, c, tm = q.popleft()
            if c >= n - 1:
                good = True
                break
            if unsafe(r, c, tm):
                continue
            for nr in (r - 1, r, r + 1):
                nc = c + 1
                nt = tm + 1
                if 0 <= nr < 3:
                    if nc >= n:
                        good = True
                        break
                    if unsafe(nr, nc, tm) or unsafe(nr, nc, nt):
                        continue
                    state = (nr, nc, nt)
                    if state not in seen:
                        seen.add(state)
                        q.append(state)

        out.append("YES" if good else "NO")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
