# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def inside(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])
    k = int(tokens[2])
    maze = [list(row) for row in tokens[3:3 + n]]

    start = None
    for r in range(n):
        for c in range(m):
            if maze[r][c] == "X":
                start = (r, c)

    if k & 1:
        sys.stdout.write("IMPOSSIBLE\n")
        return

    order = [("D", 1, 0), ("L", 0, -1), ("R", 0, 1), ("U", -1, 0)]
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    distance[start[0]][start[1]] = 0
    queue = [start]
    head = 0

    while head < len(queue):
        r, c = queue[head]
        head += 1
        for _, dr, dc in order:
            nr = r + dr
            nc = c + dc
            if inside(nr, nc, n, m) and maze[nr][nc] != "*" and distance[nr][nc] == -1:
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))

    r, c = start
    answer = []

    for remaining in range(k - 1, -1, -1):
        picked = None
        for ch, dr, dc in order:
            nr = r + dr
            nc = c + dc
            if not inside(nr, nc, n, m):
                continue
            d = distance[nr][nc]
            if d >= 0 and d <= remaining and (remaining - d) % 2 == 0:
                picked = (ch, nr, nc)
                break
        if picked is None:
            sys.stdout.write("IMPOSSIBLE\n")
            return
        answer.append(picked[0])
        r, c = picked[1], picked[2]

    sys.stdout.write("".join(answer) + "\n")

# CLAUSE: finish_program
main()
