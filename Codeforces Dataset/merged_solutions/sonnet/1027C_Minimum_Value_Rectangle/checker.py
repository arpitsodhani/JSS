"""1027C accepts any rectangle minimising P^2/S, so compare the value, not the sticks.

P^2/S = 4(a+b)^2/(ab) falls as a/b approaches 1, so the best pair is adjacent in
the sorted list of lengths that occur at least twice (a length occurring four or
more times enters that list twice and gives a square, the global optimum).
Fractions keep the comparison exact.
"""
from fractions import Fraction


def check_for(stdin, expected):
    tokens = stdin.split()
    cases = []
    pos = 1
    for _ in range(int(tokens[0])):
        n = int(tokens[pos])
        pos += 1
        cases.append([int(v) for v in tokens[pos:pos + n]])
        pos += n

    def value(a, b):
        return Fraction(4 * (a + b) * (a + b), a * b)

    def optimum(sticks):
        counts = {}
        for v in sticks:
            counts[v] = counts.get(v, 0) + 1
        pool = []
        for v in sorted(counts):
            if counts[v] >= 2:
                pool.append(v)
                if counts[v] >= 4:
                    pool.append(v)
        best = None
        for i in range(len(pool) - 1):
            here = value(pool[i], pool[i + 1])
            if best is None or here < best:
                best = here
        return best

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == 4 * len(cases), f"expected {4 * len(cases)} numbers, got {len(got)}"
        for case_no, sticks in enumerate(cases, start=1):
            chosen = got[4 * (case_no - 1):4 * case_no]
            available = {}
            for v in sticks:
                available[v] = available.get(v, 0) + 1
            for v in chosen:
                assert available.get(v, 0) > 0, f"case {case_no}: stick {v} is not available"
                available[v] -= 1
            sides = sorted(chosen)
            assert sides[0] == sides[1] and sides[2] == sides[3], (
                f"case {case_no}: {chosen} do not form a rectangle")
            here = value(sides[0], sides[2])
            best = optimum(sticks)
            assert here == best, f"case {case_no}: P^2/S is {here}, the minimum is {best}"

    return check
