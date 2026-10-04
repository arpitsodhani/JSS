"""439C accepts any partition into k parts of which exactly p have an even sum.

Feasibility is recomputed independently: the k-p odd parts each need an odd
element, the odd elements left over have to pair up, and every even part needs
either an even element or one of those pairs.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    n, k, p = (int(v) for v in tokens[:3])
    values = [int(v) for v in tokens[3:3 + n]]
    odds = sum(1 for v in values if v % 2)
    evens = n - odds
    odd_parts = k - p
    feasible = (
        odds >= odd_parts
        and (odds - odd_parts) % 2 == 0
        and evens + (odds - odd_parts) // 2 >= p
    )

    def check(out):
        lines = [line for line in out.strip().splitlines() if line.strip()]
        assert lines, "no output"
        verdict = lines[0].strip()
        if not feasible:
            assert verdict == "NO", f"a partition is impossible, printed {verdict!r}"
            return
        assert verdict == "YES", f"a partition exists, printed {verdict!r}"
        assert len(lines) == k + 1, f"expected {k} parts, got {len(lines) - 1}"
        pool = {}
        for v in values:
            pool[v] = pool.get(v, 0) + 1
        even_parts = 0
        for line in lines[1:]:
            nums = [int(v) for v in line.split()]
            count = nums[0]
            part = nums[1:]
            assert count == len(part) and count >= 1, f"bad part line {line!r}"
            for v in part:
                assert pool.get(v, 0) > 0, f"element {v} used too often"
                pool[v] -= 1
            if sum(part) % 2 == 0:
                even_parts += 1
        assert all(left == 0 for left in pool.values()), "not every element was used"
        assert even_parts == p, f"{even_parts} parts have an even sum, expected {p}"

    return check
