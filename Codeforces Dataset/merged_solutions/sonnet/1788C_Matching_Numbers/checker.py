"""1788C accepts any pairing of 1..2n whose sums are consecutive."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]
    verdicts = [line.strip().lower() for line in expected.split("\n") if line.strip().lower() in ("yes", "no")]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(len(sizes)):
            n = sizes[case]
            head = rows[at].lower()
            at += 1
            assert head == verdicts[case], f"case {case + 1}: said {head}, expected {verdicts[case]}"
            if head == "no":
                continue
            used = []
            sums = []
            for _ in range(n):
                a, b = (int(v) for v in rows[at].split())
                at += 1
                used.append(a)
                used.append(b)
                sums.append(a + b)
            assert sorted(used) == list(range(1, 2 * n + 1)), f"case {case + 1}: not a pairing of 1..2n"
            sums.sort()
            for i in range(1, n):
                assert sums[i] - sums[i - 1] == 1, f"case {case + 1}: sums are not consecutive"

    return check
