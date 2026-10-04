"""776B accepts any colouring using the fewest colours.

Two pieces must differ in colour when one price is a prime divisor of the other.
"""


def check_for(stdin, expected):
    n = int(stdin.split()[0])
    best = int(expected.split("\n")[0])

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        used = int(rows[0])
        colours = [int(v) for v in rows[1].split()]
        assert len(colours) == n, f"expected {n} colours, got {len(colours)}"
        assert len(set(colours)) == used, "the printed count does not match the colouring"
        assert used == best, f"used {used} colours, the fewest is {best}"
        for i in range(n):
            price = i + 2
            step = 2
            while step * step <= price:
                if price % step == 0:
                    break
                step += 1
            else:
                continue
            for divisor in range(2, price):
                if price % divisor:
                    continue
                simple = True
                for d in range(2, divisor):
                    if divisor % d == 0:
                        simple = False
                        break
                if simple and divisor >= 2:
                    assert colours[divisor - 2] != colours[i], \
                        f"{divisor} divides {price} but shares a colour"

    return check
