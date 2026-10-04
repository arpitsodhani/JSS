# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.buffer.read().split()
    if not parts:
        return

    n = int(parts[0])
    m = int(parts[1])
    k = int(parts[2])
    board = [line.decode() for line in parts[3:3 + n]]

    sr = sc = -1
    for i in range(n):
        j = board[i].find("X")
        if j >= 0:
            sr, sc = i, j

    if k % 2 != 0:
        sys.stdout.write("IMPOSSIBLE\n")
        return

    chars = "DLRU"
    drs = (1, 0, 0, -1)
    dcs = (0, -1, 1, 0)

    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    frontier = deque()
    frontier.append((sr, sc))

    while frontier:
        r, c = frontier.popleft()
        for idx in range(4):
            nr = r + drs[idx]
            nc = c + dcs[idx]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if board[nr][nc] == "*" or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            frontier.append((nr, nc))

    r = sr
    c = sc
    result = []

    for remaining in range(k - 1, -1, -1):
        next_r = next_c = -1
        next_char = ""
        for idx in range(4):
            nr = r + drs[idx]
            nc = c + dcs[idx]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            needed = dist[nr][nc]
            if needed >= 0 and needed <= remaining and (remaining - needed) % 2 == 0:
                next_r = nr
                next_c = nc
                next_char = chars[idx]
                break
        if next_char == "":
            sys.stdout.write("IMPOSSIBLE\n")
            return
        result.append(next_char)
        r = next_r
        c = next_c

    sys.stdout.write("".join(result) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
