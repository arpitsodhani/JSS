# CLAUSE: setup_environment
import sys
from collections import deque

def main():
    values = sys.stdin.read().split()
    pos = 0
    total = int(values[pos])
    pos += 1
    res = []

# CLAUSE: solve_logic
    for _ in range(total):
        n = int(values[pos])
        pos += 2
        board = []
        q = deque()
        for r in range(3):
            line = values[pos]
            pos += 1
            found = line.find("s")
            if found != -1:
                q.append((r, found, 0))
                line = line[:found] + "." + line[found + 1:]
            board.append(line)

        visited = [[[False] * (n + 6) for _ in range(n + 6)] for __ in range(3)]
        if q:
            visited[q[0][0]][q[0][1]][0] = True
        escaped = False

        while q:
            r, c, sec = q.popleft()
            if c >= n - 1:
                escaped = True
                break
            current = c + 2 * sec
            if current < n and board[r][current] != ".":
                continue

            for dr in (-1, 0, 1):
                nr = r + dr
                nc = c + 1
                ns = sec + 1
                if nr < 0 or nr == 3:
                    continue
                hit_now = nc + 2 * sec
                hit_next = nc + 2 * ns
                if hit_now < n and board[nr][hit_now] != ".":
                    continue
                if hit_next < n and board[nr][hit_next] != ".":
                    continue
                if nc >= n:
                    escaped = True
                    break
                if not visited[nr][nc][ns]:
                    visited[nr][nc][ns] = True
                    q.append((nr, nc, ns))
            if escaped:
                break

        res.append("YES" if escaped else "NO")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
