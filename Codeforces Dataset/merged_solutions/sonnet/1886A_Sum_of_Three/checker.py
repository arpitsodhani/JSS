"""1886A accepts any triple of distinct positive numbers, none divisible by 3."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    values = data[1:1 + data[0]]
    verdicts = [line.strip().upper() for line in expected.split("\n") if line.strip().upper() in ("YES", "NO")]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(len(values)):
            head = rows[at].upper()
            at += 1
            assert head == verdicts[case], f"case {case + 1}: said {head}, expected {verdicts[case]}"
            if head == "NO":
                continue
            x, y, z = (int(v) for v in rows[at].split())
            at += 1
            assert x + y + z == values[case], f"case {case + 1}: the sum is wrong"
            assert len({x, y, z}) == 3, f"case {case + 1}: values must be distinct"
            assert min(x, y, z) >= 1, f"case {case + 1}: values must be positive"
            assert x % 3 and y % 3 and z % 3, f"case {case + 1}: a value is divisible by 3"

    return check
