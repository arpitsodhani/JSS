"""1845A accepts any multiset of allowed integers adding up to n."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    cases = [(data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]) for i in range(t)]
    verdicts = [line.strip().upper() for line in expected.split("\n") if line.strip().upper() in ("YES", "NO")]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(t):
            n, k, x = cases[case]
            head = rows[at].upper()
            at += 1
            assert head == verdicts[case], f"case {case + 1}: said {head}, expected {verdicts[case]}"
            if head == "NO":
                continue
            count = int(rows[at])
            at += 1
            parts = [int(v) for v in rows[at].split()]
            at += 1
            assert len(parts) == count, f"case {case + 1}: said {count} parts, listed {len(parts)}"
            assert sum(parts) == n, f"case {case + 1}: parts sum to {sum(parts)}"
            assert all(1 <= v <= k and v != x for v in parts), f"case {case + 1}: a part is not allowed"

    return check
