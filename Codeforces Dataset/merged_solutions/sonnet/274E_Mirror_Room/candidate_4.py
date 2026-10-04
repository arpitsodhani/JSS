# CLAUSE: setup_environment
import sys
import bisect
from collections import defaultdict

def parse_direction(s):
    return (-1, 1) if s == b"NE" else (-1, -1) if s == b"NW" else (1, 1) if s == b"SE" else (1, -1)

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    pos = 0
    n = int(raw[pos])
    m = int(raw[pos + 1])
    k = int(raw[pos + 2])
    pos += 3
    cells = set()
    by_diff = defaultdict(list)
    by_sum = defaultdict(list)
    for _ in range(k):
        r = int(raw[pos])
        c = int(raw[pos + 1])
        pos += 2
        cells.add((r, c))
        by_diff[r - c].append(r)
        by_sum[r + c].append(r)
    start_r = int(raw[pos])
    start_c = int(raw[pos + 1])
    start_d = raw[pos + 2]

# CLAUSE: solve_logic
    if n == 1:
        barriers = [c for r, c in cells if r == 1]
        barriers.sort()
        place = bisect.bisect_left(barriers, start_c)
        a = barriers[place - 1] if place else 0
        b = barriers[place] if place < len(barriers) else m + 1
        sys.stdout.write(str(b - a - 1))
        return
    if m == 1:
        barriers = [r for r, c in cells if c == 1]
        barriers.sort()
        place = bisect.bisect_left(barriers, start_r)
        a = barriers[place - 1] if place else 0
        b = barriers[place] if place < len(barriers) else n + 1
        sys.stdout.write(str(b - a - 1))
        return

    by_diff = {key: sorted(value) for key, value in by_diff.items()}
    by_sum = {key: sorted(value) for key, value in by_sum.items()}

    def diagonal_rows(r, c, dr, dc):
        return by_diff.get(r - c, ()) if dr == dc else by_sum.get(r + c, ())

    def ray_hit_distance(r, c, dr, dc):
        if not (1 <= r <= n and 1 <= c <= m):
            return None
        rows = diagonal_rows(r, c, dr, dc)
        if dr > 0:
            p = bisect.bisect_left(rows, r)
            if p == len(rows):
                return None
            return rows[p] - r
        p = bisect.bisect_right(rows, r) - 1
        if p == -1:
            return None
        return r - rows[p]

    def solid(r, c):
        if r < 1 or c < 1 or r > n or c > m:
            return True
        return (r, c) in cells

    r, c = start_r, start_c
    dr, dc = parse_direction(start_d)
    visited_states = set()
    touched = defaultdict(list)

    while True:
        state = r, c, dr, dc
        if state in visited_states:
            break
        visited_states.add(state)
        distance = min(n - r if dr == 1 else r - 1, m - c if dc == 1 else c - 1)
        for r0, c0 in ((r + dr, c), (r, c + dc), (r + dr, c + dc)):
            v = ray_hit_distance(r0, c0, dr, dc)
            if v is not None:
                distance = min(distance, v)
        nr = r + dr * distance
        nc = c + dc * distance
        key = (0, r - c) if dr == dc else (1, r + c)
        touched[key].append((min(r, nr), max(r, nr)))
        hr = solid(nr + dr, nc)
        hc = solid(nr, nc + dc)
        hd = solid(nr + dr, nc + dc)
        if hr and hc:
            r, c, dr, dc = nr, nc, -dr, -dc
        elif hr:
            r, c, dr = nr, nc + dc, -dr
        elif hc:
            r, c, dc = nr + dr, nc, -dc
        elif hd:
            r, c, dr, dc = nr, nc, -dr, -dc
        else:
            break

    result = 0
    for group in touched.values():
        group.sort()
        l = -10
        rr = -10
        for a, b in group:
            if a > rr + 1:
                result += max(0, rr - l + 1)
                l, rr = a, b
            elif b > rr:
                rr = b
        result += max(0, rr - l + 1)

# CLAUSE: finish_program
    print(result)

if __name__ == "__main__":
    main()
