# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from functools import cmp_to_key

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n, m = data[0], data[1]
    pos = 2
    red = []
    for _ in range(n):
        red.append((data[pos], data[pos + 1]))
        pos += 2
    blue = []
    for _ in range(m):
        blue.append((data[pos], data[pos + 1]))
        pos += 2

    if n < 3:
        print(0)
        sys.exit()

    if m == 0:
        print(n * (n - 1) * (n - 2) // 6)
        sys.exit()

    def upper(dx, dy):
        return dy > 0 or (dy == 0 and dx > 0)

    def cmp_angle(a, b):
        if a[0] != b[0]:
            return -1 if a[0] else 1
        cr = a[1] * b[2] - a[2] * b[1]
        if cr > 0:
            return -1
        if cr < 0:
            return 1
        return 0

    angle_key = cmp_to_key(cmp_angle)

    left = [[0] * n for _ in range(n)]
    side = [[0] * n for _ in range(n)]

    for i, (xi, yi) in enumerate(red):
        events = []

        for j, (x, y) in enumerate(red):
            if i != j:
                dx = x - xi
                dy = y - yi
                events.append((upper(dx, dy), dx, dy, 0, j))

        for b, (x, y) in enumerate(blue):
            dx = x - xi
            dy = y - yi
            events.append((upper(dx, dy), dx, dy, 1, b))

        events.sort(key=angle_key)
        total = len(events)
        doubled = events + events

        q = 0
        blue_mask = 0
        red_mask = 0
        left_row = left[i]
        side_row = side[i]

        for p in range(total):
            if q < p + 1:
                q = p + 1

            base = doubled[p]
            bx = base[1]
            by = base[2]

            while q < p + total and bx * doubled[q][2] - by * doubled[q][1] > 0:
                e = doubled[q]
                if e[3]:
                    blue_mask |= 1 << e[4]
                else:
                    red_mask |= 1 << e[4]
                q += 1

            if base[3] == 0:
                left_row[base[4]] = blue_mask
                side_row[base[4]] = red_mask

            if q > p + 1:
                e = doubled[p + 1]
                if e[3]:
                    blue_mask ^= 1 << e[4]
                else:
                    red_mask ^= 1 << e[4]

    left_t = [[left[i][j] for i in range(n)] for j in range(n)]

    ans = 0

    for i in range(n - 2):
        left_i = left[i]
        col_i = left_t[i]
        side_i = side[i]

        for j in range(i + 1, n - 1):
            lij = left_i[j]
            lji = left[j][i]
            left_j = left[j]
            col_j = left_t[j]
            bits = side_i[j] >> (j + 1)

            for k in range(j + 1, n):
                if bits & 1:
                    if (lij & left_j[k] & col_i[k]) == 0:
                        ans += 1
                else:
                    if (lji & col_j[k] & left_i[k]) == 0:
                        ans += 1
                bits >>= 1

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
