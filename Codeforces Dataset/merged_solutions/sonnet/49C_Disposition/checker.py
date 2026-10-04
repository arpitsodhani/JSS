"""49C accepts any arrangement with the fewest divisors of the disposition."""


def check_for(stdin, expected):
    n = int(stdin.split()[0])
    wanted = [int(v) for v in expected.split()]

    def divisors(order):
        count = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                if order[j - 1] % i == 0:
                    count += 1
                    break
        return count

    best = divisors(wanted)

    def check(out):
        order = [int(v) for v in out.split()]
        assert sorted(order) == list(range(1, n + 1)), "not a permutation"
        here = divisors(order)
        assert here <= best, f"{here} divisors, the fewest is {best}"

    return check
