# Clause setup_environment [Confidence: 0.80]
import sys
import random
import time
from math import e

STEPS = ((2, 3), (2, -3), (-2, 3), (-2, -3), (3, 2), (3, -2), (-3, 2), (-3, -2))
PATTERN = ("01110", "11011", "10001", "11011", "01110")


# Clause solve_logic [Confidence: 0.80]
def is_edge(a, b):
    dr = a[0] - b[0]
    dc = a[1] - b[1]
    return dr * dr + dc * dc == 13


def initial_answer(n):
    cells = []
    for r in range(min(n, 5)):
        for c in range(min(n, 5)):
            if S[r][c] == "1":
                cells.append((r, c))
    return cells


def neighbors(n, cell):
    r, c = cell
    ans = []
    for dr, dc in D:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < n:
            ans.append((nr, nc))
    return ans


def can_attach(candidate, path, neighbor):
    for v in path:
        if v != neighbor and is_edge(candidate, v):
            return False
    return True


def construct(n, deadline):
    need = int(n * n / e)
    neigh = {}
    for r in range(n):
        for c in range(n):
            neigh[(r, c)] = neighbors(n, (r, c))

    cells = list(neigh)
    best = []

    while time.time() < deadline:
        start = random.choice(cells)
        path = deque([start])
        used = {start}

        while time.time() < deadline:
            options = []
            left = path[0]
            right = path[-1]

            for cand in neigh[left]:
                if cand not in used and can_attach(cand, path, left):
                    score = sum(1 for x in neigh[cand] if x not in used)
                    options.append((score, random.random(), -1, cand))

            for cand in neigh[right]:
                if cand not in used and can_attach(cand, path, right):
                    score = sum(1 for x in neigh[cand] if x not in used)
                    options.append((score, random.random(), 1, cand))

            if not options:
                break

            options.sort(reverse=True)
            chosen = random.choice(options[:min(6, len(options))])
            side = chosen[2]
            cell = chosen[3]

            if side < 0:
                path.appendleft(cell)
            else:
                path.append(cell)
            used.add(cell)

            if len(path) > len(best):
                best = list(path)
            if len(path) >= need and is_edge(path[0], path[-1]):
                return list(path)

    return best


def emit(n, vertices):
    rows = [["0"] * n for _ in range(n)]
    for r, c in vertices:
        rows[r][c] = "1"
    sys.stdout.write("\n".join(map("".join, rows)))


# Clause finish_program [Confidence: 0.80]
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    if n == 5:
        sys.stdout.write("\n".join(PATTERN))
        return
    if n <= 6:
        sys.stdout.write(render(n, sample_cells(n)))
        return

    random.seed(n * 1000003 + 17)
    path = make_path(n, time.time() + 8.6)
    if not path or not linked(path[0], path[-1]):
        path = sample_cells(5)
    sys.stdout.write(render(n, path))


if __name__ == "__main__":
    main()


