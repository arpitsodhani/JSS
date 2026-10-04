"""715A accepts any press plan that clears every level.

At level k the screen must stay a multiple of k after each move, the value must
be a perfect square before the root is taken, and each printed count fits 1e18.
"""


def check_for(stdin, expected):
    n = int(stdin.split()[0])

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == n, f"expected {n} numbers, got {len(got)}"
        screen = 2
        for level in range(1, n + 1):
            presses = got[level - 1]
            assert 0 <= presses <= 10 ** 18, f"level {level}: {presses} outside [0, 1e18]"
            screen += presses * level
            assert screen % level == 0, f"level {level}: {screen} is not a multiple of {level}"
            root = int(screen ** 0.5)
            while root * root > screen:
                root -= 1
            while (root + 1) * (root + 1) <= screen:
                root += 1
            assert root * root == screen, f"level {level}: {screen} is not a perfect square"
            screen = root
            assert screen % (level + 1) == 0, (
                f"after level {level}: {screen} is not a multiple of {level + 1}")

    return check
