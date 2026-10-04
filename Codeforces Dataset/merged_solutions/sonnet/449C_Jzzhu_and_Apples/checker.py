"""449C accepts any grouping of the same maximum size.

Each printed pair must share a factor above 1, apples cannot repeat, and the
number of groups has to match the reference answer.
"""


def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


def check_for(stdin, expected):
    n = int(stdin.split()[0])
    best = int(expected.split("\n")[0])

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        count = int(rows[0])
        assert count == best, f"made {count} groups, the maximum is {best}"
        seen = set()
        for i in range(count):
            x, y = (int(v) for v in rows[1 + i].split())
            assert 1 <= x <= n and 1 <= y <= n, "apple number out of range"
            assert x not in seen and y not in seen, "an apple is in two groups"
            seen.add(x)
            seen.add(y)
            assert gcd_of(x, y) > 1, f"gcd({x}, {y}) is 1"

    return check
