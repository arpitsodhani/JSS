"""1725H accepts any half-and-half colouring with a coefficient Z that no pair
of differently coloured stones matches.

concat(x, y) = x + y (mod 3) because 10^k = 1 (mod 3), so the reaction value
concat(a,b)*concat(b,a) + a*b reduces to a^2 + b^2 (mod 3); the checker uses
that and tests every cross pair.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    a = data[1:1 + n]

    def check(out):
        lines = out.split()
        assert len(lines) == 2, f"expected two lines, got {len(lines)}"
        z = int(lines[0])
        colour = lines[1]
        assert 0 <= z <= 2, f"Z={z} outside 0..2"
        assert len(colour) == n, f"colour string has length {len(colour)}"
        assert set(colour) <= {"0", "1"}, f"bad colours {colour!r}"
        assert colour.count("0") == n // 2, (
            f"{colour.count('0')} black stones, expected {n // 2}")
        black = [a[i] % 3 for i in range(n) if colour[i] == "0"]
        white = [a[i] % 3 for i in range(n) if colour[i] == "1"]
        for x in black:
            for y in white:
                value = (x * x + y * y) % 3
                assert value != z, f"stones with residues {x} and {y} react at Z={z}"

    return check
