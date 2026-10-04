"""1753A1 accepts any partition whose alternating sums add up to zero."""


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
    verdicts = [line.strip() == "-1" for line in expected.split("\n") if line.strip() == "-1" or (line.strip().isdigit() and " " not in line.strip())]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(t):
            a = cases[case]
            head = rows[at]
            at += 1
            if verdicts[case]:
                assert head == "-1", f"case {case + 1}: printed a partition where none exists"
                continue
            assert head != "-1", f"case {case + 1}: a partition exists"
            k = int(head)
            total = 0
            spot = 1
            for _ in range(k):
                low, high = (int(v) for v in rows[at].split())
                at += 1
                assert low == spot and low <= high, f"case {case + 1}: segments are not contiguous"
                sign = 1
                for i in range(low, high + 1):
                    total += sign * a[i - 1]
                    sign = -sign
                spot = high + 1
            assert spot == len(a) + 1, f"case {case + 1}: the partition does not cover the array"
            assert total == 0, f"case {case + 1}: the sums add up to {total}"

    return check
