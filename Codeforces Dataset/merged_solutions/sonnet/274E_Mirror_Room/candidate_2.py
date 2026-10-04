# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict

def direction_value(s):
    return (-1 if s[0] == 'N' else 1, 1 if s[1] == 'E' else -1)

def add_segment(store, r, c, dr, dc, length):
    key = (0, r - c) if dr == dc else (1, r + c)
    end = r + dr * length
    store[key].append((min(r, end), max(r, end)))

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    p = 0
    n, m, k = int(data[p]), int(data[p + 1]), int(data[p + 2])
    p += 3
    blocked = set()
    down = defaultdict(list)
    up = defaultdict(list)
    for _ in range(k):
        r, c = int(data[p]), int(data[p + 1])
        p += 2
        blocked.add((r, c))
        down[r - c].append(r)
        up[r + c].append(r)
    xs, ys, d = int(data[p]), int(data[p + 1]), data[p + 2].decode()

# CLAUSE: solve_logic
    if n == 1:
        cols = sorted(c for r, c in blocked if r == 1)
        q = bisect_left(cols, ys)
        print((cols[q] if q < len(cols) else m + 1) - (cols[q - 1] if q else 0) - 1)
        return
    if m == 1:
        rows = sorted(r for r, c in blocked if c == 1)
        q = bisect_left(rows, xs)
        print((rows[q] if q < len(rows) else n + 1) - (rows[q - 1] if q else 0) - 1)
        return
    for v in down.values():
        v.sort()
    for v in up.values():
        v.sort()

    def first_block(sr, sc, dr, dc):
        if sr < 1 or sr > n or sc < 1 or sc > m:
            return None
        rows = down.get(sr - sc) if dr == dc else up.get(sr + sc)
        if not rows:
            return None
        if dr > 0:
            q = bisect_left(rows, sr)
            return None if q == len(rows) else rows[q] - sr
        q = bisect_right(rows, sr) - 1
        return None if q < 0 else sr - rows[q]

    def wall(r, c):
        return r < 1 or r > n or c < 1 or c > m or (r, c) in blocked

    r, c = xs, ys
    dr, dc = direction_value(d)
    seen = set()
    segments = defaultdict(list)
    while (r, c, dr, dc) not in seen:
        seen.add((r, c, dr, dc))
        step = min(n - r if dr > 0 else r - 1, m - c if dc > 0 else c - 1)
        for sr, sc in ((r + dr, c), (r, c + dc), (r + dr, c + dc)):
            got = first_block(sr, sc, dr, dc)
            if got is not None and got < step:
                step = got
        add_segment(segments, r, c, dr, dc, step)
        nr, nc = r + dr * step, c + dc * step
        hit_r = wall(nr + dr, nc)
        hit_c = wall(nr, nc + dc)
        hit_d = wall(nr + dr, nc + dc)
        if hit_r and hit_c:
            r, c, dr, dc = nr, nc, -dr, -dc
        elif hit_r:
            r, c, dr = nr, nc + dc, -dr
        elif hit_c:
            r, c, dc = nr + dr, nc, -dc
        elif hit_d:
            r, c, dr, dc = nr, nc, -dr, -dc
        else:
            break

    ans = 0
    for a in segments.values():
        a.sort()
        left = right = None
        for x, y in a:
            if left is None:
                left, right = x, y
            elif x <= right + 1:
                right = max(right, y)
            else:
                ans += right - left + 1
                left, right = x, y
        if left is not None:
            ans += right - left + 1

# CLAUSE: finish_program
    print(ans)

if __name__ == "__main__":
    main()
