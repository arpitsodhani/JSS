"""375A accepts any digit rearrangement divisible by 7 without leading zeroes."""


def check_for(stdin, expected):
    source = stdin.strip()

    def check(out):
        got = out.strip()
        assert got, "no answer printed"
        assert sorted(got) == sorted(source), "the digits were not rearranged"
        assert got[0] != "0", "leading zero"
        assert int(got) % 7 == 0, f"{got} is not divisible by 7"

    return check
