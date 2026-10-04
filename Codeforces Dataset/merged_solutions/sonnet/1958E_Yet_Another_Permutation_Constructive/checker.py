"""1958E accepts any permutation that collapses to [n] after exactly k rounds.

A round keeps only the elements that are larger than both neighbours, so the
checker replays the rounds; -1 is right exactly when 2^(k-1) >= n, the largest
size a k-round permutation can have.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    cases = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(data[0])]

    def rounds(perm):
        steps = 0
        while len(perm) > 1:
            perm = [v for i, v in enumerate(perm)
                    if (i == 0 or v > perm[i - 1]) and (i == len(perm) - 1 or v > perm[i + 1])]
            steps += 1
        return steps

    def check(out):
        lines = [line for line in out.strip().splitlines() if line.strip()]
        assert len(lines) == len(cases), f"expected {len(cases)} lines, got {len(lines)}"
        for idx, ((n, k), line) in enumerate(zip(cases, lines), start=1):
            possible = (1 << (k - 1)) < n
            if not possible:
                assert line.strip() == "-1", f"case {idx}: expected -1, got {line!r}"
                continue
            perm = [int(v) for v in line.split()]
            assert sorted(perm) == list(range(1, n + 1)), f"case {idx}: not a permutation of 1..{n}"
            got = rounds(perm)
            assert got == k, f"case {idx}: collapses in {got} rounds, expected {k}"

    return check
