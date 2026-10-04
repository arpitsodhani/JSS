"""1530D accepts any derangement-style assignment with the most wishes met."""


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
    wanted = [int(line) for line in expected.split("\n") if line.strip() and " " not in line.strip()]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(t):
            wishes = cases[case]
            n = len(wishes)
            count = int(rows[at])
            given = [int(v) for v in rows[at + 1].split()]
            at += 2
            assert sorted(given) == list(range(1, n + 1)), f"case {case + 1}: not a permutation"
            for i in range(n):
                assert given[i] != i + 1, f"case {case + 1}: employee {i + 1} got themselves"
            happy = sum(1 for i in range(n) if given[i] == wishes[i])
            assert happy == count, f"case {case + 1}: printed {count} but met {happy} wishes"
            assert count >= wanted[case], f"case {case + 1}: met {count}, best is {wanted[case]}"

    return check
