"""1714D accepts any fewest-steps colouring of the whole text."""


def check_for(stdin, expected):
    data = stdin.split()
    q = int(data[0])
    pos = 1
    cases = []
    for _ in range(q):
        text = data[pos]
        n = int(data[pos + 1])
        pos += 2
        pieces = [data[pos + i] for i in range(n)]
        pos += n
        cases.append((text, pieces))
    rows = [line.strip() for line in expected.split("\n") if line.strip()]
    wanted = []
    at = 0
    for text, pieces in cases:
        value = int(rows[at])
        wanted.append(value)
        at += 1 if value < 0 else 1 + value

    def check(out):
        lines = [line.strip() for line in out.split("\n") if line.strip()]
        spot = 0
        for case in range(q):
            text, pieces = cases[case]
            count = int(lines[spot])
            spot += 1
            if wanted[case] < 0:
                assert count == -1, f"case {case + 1}: printed steps where none exist"
                continue
            assert count == wanted[case], f"case {case + 1}: used {count} steps, best is {wanted[case]}"
            painted = [False] * len(text)
            for _ in range(count):
                index, start = (int(v) for v in lines[spot].split())
                spot += 1
                assert 1 <= index <= len(pieces), f"case {case + 1}: bad string index"
                piece = pieces[index - 1]
                assert 1 <= start and start + len(piece) - 1 <= len(text), f"case {case + 1}: out of range"
                assert text[start - 1:start - 1 + len(piece)] == piece, f"case {case + 1}: no occurrence there"
                for i in range(start - 1, start - 1 + len(piece)):
                    painted[i] = True
            assert all(painted), f"case {case + 1}: the text is not fully coloured"

    return check
