"""1107A accepts any split into at least two strictly increasing numbers.

Only length-two strings can fail (their two digits must increase), so the
checker recomputes that and then validates the printed pieces.
"""


def check_for(stdin, expected):
    data = stdin.split()
    q = int(data[0])
    cases = []
    pos = 1
    for _ in range(q):
        pos += 1
        cases.append(data[pos])
        pos += 1

    def check(out):
        tokens = out.split()
        at = 0
        for s in cases:
            possible = len(s) > 2 or s[0] < s[1]
            verdict = tokens[at].upper()
            at += 1
            if not possible:
                assert verdict == "NO", f"{s!r}: expected NO, got {verdict}"
                continue
            assert verdict == "YES", f"{s!r}: expected YES, got {verdict}"
            count = int(tokens[at])
            at += 1
            assert count >= 2, f"{s!r}: only {count} parts"
            parts = tokens[at:at + count]
            at += count
            assert "".join(parts) == s, f"{s!r}: parts {parts} do not concatenate back"
            values = [int(p) for p in parts]
            assert all(values[i] < values[i + 1] for i in range(count - 1)), (
                f"{s!r}: parts {parts} are not increasing")
        assert at == len(tokens), "extra output"

    return check
