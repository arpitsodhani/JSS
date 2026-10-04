# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        it = iter(data)
        t = next(it)
        out = []

        for _ in range(t):
            n = next(it)
            ax = next(it)
            ay = next(it)
            bx = next(it)
            by = next(it)

            xs = [next(it) for _ in range(n)]
            groups = {}

            for x in xs:
                y = next(it)
                if x in groups:
                    lo, hi = groups[x]
                    if y < lo:
                        lo = y
                    if y > hi:
                        hi = y
                    groups[x] = (lo, hi)
                else:
                    groups[x] = (y, y)

            cols = [(ax, ay, ay)]
            for x in sorted(groups):
                lo, hi = groups[x]
                cols.append((x, lo, hi))
            cols.append((bx, by, by))

            dp_hi = 0
            dp_lo = 0
            prev_x, prev_lo, prev_hi = cols[0]

            for x, lo, hi in cols[1:]:
                width = hi - lo
                to_hi = min(
                    dp_hi + abs(x - prev_x) + abs(prev_hi - lo),
                    dp_lo + abs(x - prev_x) + abs(prev_lo - lo)
                ) + width
                to_lo = min(
                    dp_hi + abs(x - prev_x) + abs(prev_hi - hi),
                    dp_lo + abs(x - prev_x) + abs(prev_lo - hi)
                ) + width

                dp_hi, dp_lo = to_hi, to_lo
                prev_x, prev_lo, prev_hi = x, lo, hi

            out.append(str(min(dp_hi, dp_lo)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
