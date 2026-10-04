"""1387B1 accepts any assignment reaching the smallest total distance.

The printed permutation has to be a derangement, and the sum of tree distances
between old and new houses has to match the reference total.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = data[1 + 2 * i]
        b = data[2 + 2 * i]
        adj[a].append(b)
        adj[b].append(a)
    best = int(expected.split("\n")[0])

    def distance(src, dst):
        seen = [False] * (n + 1)
        seen[src] = True
        frontier = [src]
        step = 0
        while frontier:
            if dst in frontier:
                return step
            nxt = []
            for v in frontier:
                for u in adj[v]:
                    if not seen[u]:
                        seen[u] = True
                        nxt.append(u)
            frontier = nxt
            step += 1
        return -1

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        total = int(rows[0])
        moves = [int(v) for v in rows[1].split()]
        assert len(moves) == n, f"expected {n} houses, got {len(moves)}"
        assert sorted(moves) == list(range(1, n + 1)), "not a permutation"
        for i in range(n):
            assert moves[i] != i + 1, f"villager {i + 1} did not move"
        walked = sum(distance(i + 1, moves[i]) for i in range(n))
        assert walked == total, f"printed {total} but the assignment walks {walked}"
        assert total == best, f"total {total}, the smallest is {best}"

    return check
