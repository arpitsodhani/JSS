"""1699A accepts any valid triple. Every bit contributes 0 or 2 to the sum, so an
odd n is impossible and -1 is then the only correct answer."""


def check_for(stdin, expected):
    values = [int(v) for v in stdin.split()[1:]]

    def check(out):
        got = out.split()
        at = 0
        for n in values:
            if n % 2:
                assert got[at] == "-1", f"n={n} is odd, so -1 is the only answer"
                at += 1
                continue
            a, b, c = (int(got[at + i]) for i in range(3))
            at += 3
            for v in (a, b, c):
                assert 0 <= v <= 10 ** 9, f"n={n}: {v} outside [0, 1e9]"
            total = (a ^ b) + (b ^ c) + (a ^ c)
            assert total == n, f"n={n}: ({a},{b},{c}) gives {total}"
        assert at == len(got), "trailing output"

    return check
