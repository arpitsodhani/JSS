"""2192B accepts any set of distinct indices whose operations clear the string."""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = [data[2 + 2 * i] for i in range(t)]
    rows = [line for line in expected.split("\n")]
    possible = []
    at = 0
    for _ in range(t):
        while rows[at].strip() == "":
            at += 1
        head = rows[at].strip()
        at += 1
        if head == "-1":
            possible.append(False)
        else:
            possible.append(True)
            at += 1

    def check(out):
        lines = out.split("\n")
        pos = 0
        for case in range(t):
            while lines[pos].strip() == "":
                pos += 1
            head = lines[pos].strip()
            pos += 1
            if not possible[case]:
                assert head == "-1", f"case {case + 1}: claimed a solution where none exists"
                continue
            assert head != "-1", f"case {case + 1}: a solution exists but -1 was printed"
            count = int(head)
            spots = lines[pos].split() if pos < len(lines) else []
            pos += 1
            s = cases[case]
            assert len(spots) == count, f"case {case + 1}: listed {len(spots)} indices, said {count}"
            chosen = set()
            for value in spots:
                index = int(value)
                assert 1 <= index <= len(s), f"case {case + 1}: index {index} out of range"
                assert index not in chosen, f"case {case + 1}: index {index} chosen twice"
                chosen.add(index)
            for i in range(len(s)):
                flips = count - (1 if i + 1 in chosen else 0)
                assert (int(s[i]) + flips) % 2 == 0, f"case {case + 1}: bit {i + 1} is left at 1"

    return check
