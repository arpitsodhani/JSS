"""1152B accepts any plan of at most 40 alternating operations that ends on 2^m-1.

Odd-numbered steps XOR x with 2^n - 1 for a printed n; even-numbered steps add 1.
"""


def check_for(stdin, expected):
    start = int(stdin.split()[0])

    def check(out):
        got = [int(v) for v in out.split()]
        steps = got[0]
        assert 0 <= steps <= 40, f"{steps} operations is outside [0, 40]"
        picks = got[1:]
        assert len(picks) == (steps + 1) // 2, (
            f"expected {(steps + 1) // 2} exponents, got {len(picks)}")
        x = start
        at = 0
        for step in range(1, steps + 1):
            if step % 2:
                n = picks[at]
                at += 1
                assert 0 <= n <= 30, f"exponent {n} outside [0, 30]"
                x ^= (1 << n) - 1
            else:
                x += 1
        assert x & (x + 1) == 0, f"ended at {x}, which is not 2^m - 1"

    return check
