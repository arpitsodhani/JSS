"""1583F accepts any optimal colouring, so check the count and the property.

A colouring is valid when no monochromatic path has k or more edges; since every
edge runs from a lower label to a higher one, the longest monochromatic path is a
one-pass DP over the nodes in increasing order. The minimum number of colours is
ceil(log_k n), computed here by repeated multiplication.
"""


def check_for(stdin, expected):
    n, k = (int(x) for x in stdin.split())
    colours_needed, reach = 0, 1
    while reach < n:
        reach *= k
        colours_needed += 1
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]

    def check(out):
        got = [int(x) for x in out.split()]
        assert got, "empty output"
        count = got[0]
        assert count == colours_needed, f"used {count} colours, the minimum is {colours_needed}"
        colours = got[1:]
        assert len(colours) == len(pairs), f"expected {len(pairs)} edge colours, got {len(colours)}"
        assert set(colours) == set(range(1, count + 1)), (
            f"colours present are {sorted(set(colours))}, expected exactly 1..{count}")
        by_colour = {}
        for (a, b), colour in zip(pairs, colours):
            by_colour.setdefault(colour, []).append((a, b))
        for colour, edges in by_colour.items():
            best = [0] * n
            for a, b in edges:
                if best[a] + 1 > best[b]:
                    best[b] = best[a] + 1
            longest = max(best)
            assert longest < k, (
                f"colour {colour} carries a monochromatic path of {longest} edges, k={k}")

    return check
