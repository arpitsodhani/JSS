"""1497C2 accepts any k positive parts summing to n whose LCM is at most n/2."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    cases = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]

    def gcd_of(a, b):
        while b:
            a, b = b, a % b
        return a

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            n, k = cases[case]
            parts = [int(v) for v in rows[case]]
            assert len(parts) == k, f"case {case + 1}: expected {k} parts, got {len(parts)}"
            assert all(v >= 1 for v in parts), f"case {case + 1}: parts must be positive"
            assert sum(parts) == n, f"case {case + 1}: parts sum to {sum(parts)}, expected {n}"
            lcm = 1
            for value in parts:
                lcm = lcm * value // gcd_of(lcm, value)
                if lcm > n:
                    break
            assert lcm * 2 <= n, f"case {case + 1}: lcm {lcm} exceeds n/2"

    return check
