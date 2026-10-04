"""1196B accepts any split into k pieces of odd sum, so check the cut points."""


def check_for(stdin, expected):
    tokens = [int(v) for v in stdin.split()]
    cases = []
    pos = 1
    for _ in range(tokens[0]):
        n, k = tokens[pos], tokens[pos + 1]
        pos += 2
        cases.append((n, k, tokens[pos:pos + n]))
        pos += n

    def check(out):
        rows = out.strip().split("\n")
        at = 0
        for n, k, values in cases:
            head = rows[at].strip().upper()
            at += 1
            odd = sum(1 for v in values if v % 2)
            possible = odd >= k and (odd - k) % 2 == 0
            if head == "NO":
                assert not possible, "printed NO but a split exists"
                continue
            assert head == "YES", f"unexpected line {head!r}"
            assert possible, "printed YES but no split exists"
            cuts = [int(v) for v in rows[at].split()]
            at += 1
            assert len(cuts) == k, f"expected {k} cut points, got {len(cuts)}"
            assert cuts[-1] == n, "the last cut must be n"
            assert all(cuts[i] < cuts[i + 1] for i in range(k - 1)), "cuts must increase"
            start = 0
            for cut in cuts:
                assert cut > start, "empty piece"
                assert sum(values[start:cut]) % 2 == 1, f"piece [{start + 1}, {cut}] has even sum"
                start = cut

    return check
