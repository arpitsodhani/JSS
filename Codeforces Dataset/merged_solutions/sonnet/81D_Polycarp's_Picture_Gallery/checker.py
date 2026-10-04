"""81D accepts any valid gallery, so check the rules.

A cyclic arrangement with no two equal neighbours exists exactly when the albums
can supply n photos with no album contributing more than floor(n/2), so -1 is
correct precisely when sum(min(a_i, n // 2)) < n.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    m = int(tokens[1])
    albums = [int(x) for x in tokens[2:2 + m]]
    feasible = sum(min(x, n // 2) for x in albums) >= n

    def check(out):
        got = out.split()
        if len(got) == 1 and got[0] == "-1":
            assert not feasible, "printed -1 but a gallery exists"
            return
        assert feasible, "printed a gallery but no arrangement is possible"
        picks = [int(x) for x in got]
        assert len(picks) == n, f"expected {n} photos, got {len(picks)}"
        used = [0] * (m + 1)
        for value in picks:
            assert 1 <= value <= m, f"album {value} does not exist"
            used[value] += 1
        for i in range(m):
            assert used[i + 1] <= albums[i], (
                f"album {i + 1} used {used[i + 1]} times but holds only {albums[i]}")
        for i in range(n):
            assert picks[i] != picks[(i + 1) % n], (
                f"positions {i + 1} and {(i + 1) % n + 1} are both album {picks[i]}")

    return check
