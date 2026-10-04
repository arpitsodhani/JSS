"""1312B accepts any good shuffle, so the printed order is checked directly.

It has to be a rearrangement of the input, with all values of i - a_i distinct.
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
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            a = cases[case]
            got = [int(v) for v in rows[case]]
            assert sorted(got) == sorted(a), f"case {case + 1}: not a shuffle of the input"
            marks = [i - got[i] for i in range(len(got))]
            assert len(set(marks)) == len(marks), f"case {case + 1}: two indices collide"

    return check
