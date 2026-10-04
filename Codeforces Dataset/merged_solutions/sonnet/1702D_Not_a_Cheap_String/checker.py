"""1702D accepts any longest affordable subsequence of the word."""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = [(data[1 + 2 * i], int(data[2 + 2 * i])) for i in range(t)]
    reference = expected.split("\n")

    def check(out):
        rows = out.split("\n")
        for case in range(t):
            word, budget = cases[case]
            got = rows[case].strip()
            want = reference[case].strip()
            price = sum(ord(ch) - 96 for ch in got)
            assert price <= budget, f"case {case + 1}: price {price} exceeds {budget}"
            at = 0
            for ch in got:
                at = word.index(ch, at) + 1
            assert len(got) == len(want), f"case {case + 1}: kept {len(got)} letters, best is {len(want)}"

    return check
