# Clause setup_environment [Confidence: 0.60]
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


# Clause solve_logic [Confidence: 0.80]
    if min(n, m) == 1:
        values = []
        current = c if n == 1 else r
        border = m if n == 1 else n
        for br, bc in bad:
            if n == 1:
                values.append(bc)
            elif bc == 1:
                values.append(br)
        values.sort()
        j = bisect_left(values, current)
        before = values[j - 1] if j else 0
        after = values[j] if j < len(values) else border + 1
        print(after - before - 1)
        return

    for one in diagonals:
        for key in one:
            one[key].sort()

    def kind_and_const(a, b, vr, vc):
        if vr == vc:
            return 0, a - b
        return 1, a + b

    def next_bad(a, b, vr, vc):
        if a < 1 or b < 1 or a > n or b > m:
            return None
        typ, key = kind_and_const(a, b, vr, vc)
        arr = diagonals[typ].get(key)
        if not arr:
            return None
        if vr > 0:
            j = bisect_left(arr, a)
            return None if j >= len(arr) else arr[j] - a
        j = bisect_right(arr, a) - 1
        return None if j < 0 else a - arr[j]

    def occupied(a, b):
        return a < 1 or b < 1 or a > n or b > m or (a, b) in bad

    paths = defaultdict(list)
    states = set()

    while True:
        state = (r, c, dr, dc)
        if state in states:
            break
        states.add(state)
        row_room = n - r if dr > 0 else r - 1
        col_room = m - c if dc > 0 else c - 1
        length = row_room if row_room < col_room else col_room
        a = next_bad(r + dr, c, dr, dc)
        b = next_bad(r, c + dc, dr, dc)
        e = next_bad(r + dr, c + dc, dr, dc)
        for z in (a, b, e):
            if z is not None and z < length:
                length = z
        nr = r + dr * length
        nc = c + dc * length
        typ, key = kind_and_const(r, c, dr, dc)
        lo, hi = (r, nr) if r <= nr else (nr, r)
        paths[(typ, key)].append((lo, hi))
        xhit = occupied(nr + dr, nc)
        yhit = occupied(nr, nc + dc)
        dhit = occupied(nr + dr, nc + dc)
        if xhit and yhit:
            r, c = nr, nc
            dr, dc = -dr, -dc
        elif xhit:
            r, c = nr, nc + dc
            dr = -dr
        elif yhit:
            r, c = nr + dr, nc
            dc = -dc
        elif dhit:
            r, c = nr, nc
            dr, dc = -dr, -dc
        else:
            break

    answer = 0
    for intervals in paths.values():
        intervals.sort()
        stack_l = None
        stack_r = None
        for lo, hi in intervals:
            if stack_l is None:
                stack_l, stack_r = lo, hi
            elif lo <= stack_r + 1:
                if hi > stack_r:
                    stack_r = hi
            else:
                answer += stack_r - stack_l + 1
                stack_l, stack_r = lo, hi
        if stack_l is not None:
            answer += stack_r - stack_l + 1


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    main()


