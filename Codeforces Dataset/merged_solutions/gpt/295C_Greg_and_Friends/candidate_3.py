# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque
    from math import comb

    MOD = 1000000007

    data = list(map(int, sys.stdin.read().split()))
    n, k = data[0], data[1]
    weights = data[2:]

    c50 = weights.count(50)
    c100 = weights.count(100)
    cap = k // 50

    moves = []
    for x in range(c50 + 1):
        for y in range(c100 + 1):
            if x + y > 0 and x + 2 * y <= cap:
                moves.append((x, y))

    dist = [[[-1] * 2 for _ in range(c100 + 1)] for __ in range(c50 + 1)]
    ways = [[[0] * 2 for _ in range(c100 + 1)] for __ in range(c50 + 1)]

    dist[c50][c100][0] = 0
    ways[c50][c100][0] = 1
    q = deque([(c50, c100, 0)])

    while q:
        a, b, side = q.popleft()
        d = dist[a][b][side]

        for x, y in moves:
            if side == 0:
                if x <= a and y <= b:
                    na, nb, ns = a - x, b - y, 1
                    add = comb(a, x) * comb(b, y)
                else:
                    continue
            else:
                ra, rb = c50 - a, c100 - b
                if x <= ra and y <= rb:
                    na, nb, ns = a + x, b + y, 0
                    add = comb(ra, x) * comb(rb, y)
                else:
                    continue

            if dist[na][nb][ns] == -1:
                dist[na][nb][ns] = d + 1
                q.append((na, nb, ns))

            if dist[na][nb][ns] == d + 1:
                ways[na][nb][ns] = (ways[na][nb][ns] + ways[a][b][side] * add) % MOD

    print(dist[0][0][1])
    print(ways[0][0][1] if dist[0][0][1] != -1 else 0)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
