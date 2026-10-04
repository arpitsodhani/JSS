"""1276A accepts any minimum-size set of positions whose removal kills every "one"/"two"."""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = [data[1 + i] for i in range(t)]
    rows = expected.split("\n")
    wanted = []
    at = 0
    for _ in range(t):
        while rows[at].strip() == "":
            at += 1
        count = int(rows[at].strip())
        at += 2
        wanted.append(count)

    def check(out):
        lines = out.split("\n")
        pos = 0
        for case in range(t):
            while lines[pos].strip() == "":
                pos += 1
            count = int(lines[pos].strip())
            pos += 1
            spots = lines[pos].split() if pos < len(lines) else []
            pos += 1
            assert count == wanted[case], f"case {case + 1}: removed {count}, minimum is {wanted[case]}"
            assert len(spots) == count, f"case {case + 1}: listed {len(spots)} positions, said {count}"
            s = cases[case]
            drop = set()
            for value in spots:
                index = int(value)
                assert 1 <= index <= len(s), f"case {case + 1}: position {index} out of range"
                assert index not in drop, f"case {case + 1}: position {index} repeated"
                drop.add(index)
            rest = "".join(s[i] for i in range(len(s)) if i + 1 not in drop)
            assert "one" not in rest and "two" not in rest, f"case {case + 1}: {rest!r} is still disliked"

    return check
