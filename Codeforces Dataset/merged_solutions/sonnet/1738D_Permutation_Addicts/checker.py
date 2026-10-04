"""1738D accepts any permutation and threshold that produce the given b.

So the printed pair is replayed through the definition of b and compared with
the sequence from the input.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n

    def check(out):
        numbers = [int(v) for v in out.split()]
        at = 0
        for case in range(t):
            b = cases[case]
            n = len(b)
            k = numbers[at]
            at += 1
            a = numbers[at:at + n]
            at += n
            assert 0 <= k <= n, f"case {case + 1}: threshold {k} out of range"
            assert sorted(a) == list(range(1, n + 1)), f"case {case + 1}: not a permutation"
            built = [0] * (n + 1)
            last_small = 0
            last_big = n + 1
            for x in a:
                if x <= k:
                    built[x] = last_big
                    last_small = x
                else:
                    built[x] = last_small
                    last_big = x
            assert built[1:] == b, f"case {case + 1}: rebuilt {built[1:]}, wanted {b}"

    return check
