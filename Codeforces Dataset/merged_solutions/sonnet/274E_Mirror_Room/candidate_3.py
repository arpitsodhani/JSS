# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right

def move_delta(word):
    a = -1 if word[0] == 78 else 1
    b = 1 if word[1] == 69 else -1
    return a, b

def interval_key(r, c, dr, dc):
    if dr == dc:
        return 0, r - c
    return 1, r + c

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    blocked = set()
    lines = {}
    for _ in range(k):
        r = int(next(it))
        c = int(next(it))
        blocked.add((r, c))
        lines.setdefault((0, r - c), []).append(r)
        lines.setdefault((1, r + c), []).append(r)
    x = int(next(it))
    y = int(next(it))
    direction = next(it)

# CLAUSE: solve_logic
    if n == 1 or m == 1:
        fixed = 1
        vals = []
        here = y if n == 1 else x
        limit = m if n == 1 else n
        for r, c in blocked:
            if (n == 1 and r == fixed) or (m == 1 and c == fixed):
                vals.append(c if n == 1 else r)
        vals.sort()
        pos = bisect_left(vals, here)
        lo = vals[pos - 1] if pos else 0
        hi = vals[pos] if pos < len(vals) else limit + 1
        print(hi - lo - 1)
        return

    for rows in lines.values():
        rows.sort()

    def obstacle_distance(sr, sc, dr, dc):
        if sr < 1 or sc < 1 or sr > n or sc > m:
            return None
        rows = lines.get(interval_key(sr, sc, dr, dc))
        if rows is None:
            return None
        if dr == 1:
            pos = bisect_left(rows, sr)
            if pos == len(rows):
                return None
            return rows[pos] - sr
        pos = bisect_right(rows, sr) - 1
        if pos < 0:
            return None
        return sr - rows[pos]

    def blocked_or_border(r, c):
        return r <= 0 or c <= 0 or r > n or c > m or (r, c) in blocked

    dr, dc = move_delta(direction)
    used_states = set()
    covered = {}
    while True:
        state = (x, y, dr, dc)
        if state in used_states:
            break
        used_states.add(state)
        stop = n - x if dr == 1 else x - 1
        col_stop = m - y if dc == 1 else y - 1
        if col_stop < stop:
            stop = col_stop
        checks = ((dr, 0), (0, dc), (dr, dc))
        for ar, ac in checks:
            dist = obstacle_distance(x + ar, y + ac, dr, dc)
            if dist is not None and dist < stop:
                stop = dist
        key = interval_key(x, y, dr, dc)
        end_row = x + dr * stop
        covered.setdefault(key, []).append((x, end_row) if x <= end_row else (end_row, x))
        px = x + dr * stop
        py = y + dc * stop
        side_r = blocked_or_border(px + dr, py)
        side_c = blocked_or_border(px, py + dc)
        corner = blocked_or_border(px + dr, py + dc)
        if side_r and side_c:
            x, y = px, py
            dr = -dr
            dc = -dc
        elif side_r:
            x, y = px, py + dc
            dr = -dr
        elif side_c:
            x, y = px + dr, py
            dc = -dc
        elif corner:
            x, y = px, py
            dr = -dr
            dc = -dc
        else:
            break

    total = 0
    for ranges in covered.values():
        ranges.sort()
        merged = []
        for l, r in ranges:
            if merged and l <= merged[-1][1] + 1:
                if r > merged[-1][1]:
                    merged[-1] = (merged[-1][0], r)
            else:
                merged.append((l, r))
        for l, r in merged:
            total += r - l + 1

# CLAUSE: finish_program
    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()
