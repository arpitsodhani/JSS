# CLAUSE: setup_environment
import sys
import random
import time
from math import e

MOVE_LIST = [(2, 3), (2, -3), (-2, 3), (-2, -3), (3, 2), (3, -2), (-3, 2), (-3, -2)]
BASE = ["01110", "11011", "10001", "11011", "01110"]


# CLAUSE: solve_logic
def edge(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 == 13


def inside(n, x, y):
    return 0 <= x < n and 0 <= y < n


def conflicts(candidate, vertices, allowed):
    for old in vertices:
        if old != allowed and edge(candidate, old):
            return True
    return False


def next_vertices(n, point):
    r, c = point
    for dr, dc in MOVE_LIST:
        nr = r + dr
        nc = c + dc
        if inside(n, nr, nc):
            yield nr, nc


def freedom_score(n, point, used):
    total = 0
    for nxt in next_vertices(n, point):
        if nxt not in used:
            total += 1
    return total


def search(n, stop_at):
    want = int(n * n / e)
    starts = [(r, c) for r in range(n) for c in range(n)]
    best = None

    while time.time() < stop_at:
        route = [random.choice(starts)]
        used = {route[0]}

        while time.time() < stop_at:
            pool = []
            ends = ((0, route[0]), (1, route[-1]))
            for side, end in ends:
                for cand in next_vertices(n, end):
                    if cand in used or conflicts(cand, route, end):
                        continue
                    pool.append((freedom_score(n, cand, used), random.random(), side, cand))

            if len(pool) == 0:
                break

            pool.sort(key=lambda x: (x[0], x[1]), reverse=True)
            side = None
            cand = None
            pick = random.randrange(min(6, len(pool)))
            side = pool[pick][2]
            cand = pool[pick][3]

            if side == 0:
                route = [cand] + route
            else:
                route.append(cand)
            used.add(cand)

            if best is None or len(route) > len(best):
                best = route[:]
            if len(route) >= want and edge(route[0], route[-1]):
                return route

    return best


def grid_from(n, chosen):
    chosen = set(chosen)
    lines = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append("1" if (r, c) in chosen else "0")
        lines.append("".join(row))
    return "\n".join(lines)


def base_vertices(size):
    out = []
    for r, row in enumerate(BASE[:size]):
        for c, value in enumerate(row[:size]):
            if value == "1":
                out.append((r, c))
    return out


# CLAUSE: finish_program
def main():
    raw = sys.stdin.read().strip().split()
    if not raw:
        return
    n = int(raw[0])

    if n == 5:
        print("\n".join(BASE), end="")
        return

    if n <= 6:
        print(grid_from(n, base_vertices(n)), end="")
        return

    random.seed(1000003 * n + 17)
    answer = search(n, time.time() + 8.6)
    if answer is None or not edge(answer[0], answer[-1]):
        answer = base_vertices(5)
    print(grid_from(n, answer), end="")


if __name__ == "__main__":
    main()
