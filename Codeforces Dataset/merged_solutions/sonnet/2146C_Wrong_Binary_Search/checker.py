"""2146C accepts any permutation whose stable positions are exactly the ones
marked 1.

Position x is stable exactly when p[x] = x and p[1..x] is a permutation of
1..x, which the checker tests with a running prefix maximum. A run of zeros of
length one forces a fixed point, so those inputs must answer NO.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        cases.append((n, s))

    def feasible(s):
        i = 0
        while i < len(s):
            if s[i] == "1":
                i += 1
                continue
            j = i
            while j < len(s) and s[j] == "0":
                j += 1
            if j - i == 1:
                return False
            i = j
        return True

    def check(out):
        tokens = out.split()
        pos = 0
        for n, s in cases:
            verdict = tokens[pos]
            pos += 1
            if not feasible(s):
                assert verdict == "NO", f"expected NO for {s!r}, got {verdict!r}"
                continue
            assert verdict == "YES", f"expected YES for {s!r}, got {verdict!r}"
            p = [int(v) for v in tokens[pos:pos + n]]
            pos += n
            assert sorted(p) == list(range(1, n + 1)), "not a permutation"
            highest = 0
            for i in range(n):
                if p[i] > highest:
                    highest = p[i]
                stable = p[i] == i + 1 and highest == i + 1
                assert stable == (s[i] == "1"), (
                    f"position {i+1} stable={stable} but s says {s[i]}")
        assert pos == len(tokens), "extra output"

    return check
