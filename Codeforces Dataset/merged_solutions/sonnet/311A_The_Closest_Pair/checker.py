"""311A accepts any n points that push the sample code's counter above k.

The checker replays the pseudo-code from the statement on the printed points and
compares its operation count with k; "no solution" is right exactly when even the
best possible layout, n(n-1)/2 comparisons, does not exceed k.
"""


def check_for(stdin, expected):
    n, k = (int(v) for v in stdin.split()[:2])
    possible = n * (n - 1) // 2 > k

    def check(out):
        text = out.strip()
        if not possible:
            assert text == "no solution", f"a layout exists, printed {text[:30]!r}"
            return
        assert text != "no solution", "printed 'no solution' but a layout exists"
        rows = [line.split() for line in text.splitlines() if line.strip()]
        assert len(rows) == n, f"expected {n} points, got {len(rows)}"
        pts = []
        for row in rows:
            assert len(row) == 2, f"bad point line {row}"
            x, y = int(row[0]), int(row[1])
            assert abs(x) <= 10 ** 9 and abs(y) <= 10 ** 9, "coordinate out of range"
            pts.append((x, y))
        pts.sort()
        total = 0
        best = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                total += 1
                if pts[j][0] - pts[i][0] >= best:
                    break
                dx = pts[j][0] - pts[i][0]
                dy = pts[j][1] - pts[i][1]
                here = (dx * dx + dy * dy) ** 0.5
                if here < best:
                    best = here
        assert total > k, f"the code runs {total} comparisons, needs more than {k}"

    return check
