"""1453D accepts any stage layout of at most 2000 stages with expected tries k."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    cases = data[1:1 + data[0]]

    def check(out):
        rows = [line for line in out.split("\n")]
        at = 0
        for case in range(len(cases)):
            while rows[at].strip() == "":
                at += 1
            head = rows[at].strip()
            at += 1
            k = cases[case]
            if head == "-1":
                assert k % 2 == 1, f"case {case + 1}: said impossible for k={k}"
                continue
            n = int(head)
            stages = [int(v) for v in rows[at].split()]
            at += 1
            assert 1 <= n <= 2000, f"case {case + 1}: {n} stages is out of range"
            assert len(stages) == n, f"case {case + 1}: listed {len(stages)} stages, said {n}"
            assert set(stages) <= {0, 1}, f"case {case + 1}: stages must be 0 or 1"
            assert stages[0] == 1, f"case {case + 1}: stage 1 must hold a checkpoint"
            total = 0
            block = 0
            for value in stages + [1]:
                if value == 1 and block:
                    total += (1 << (block + 1)) - 2
                    block = 0
                block += 1
            assert total == k, f"case {case + 1}: expected tries {total}, wanted {k}"

    return check
