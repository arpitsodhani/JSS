"""Judge side of 1534D, an interactive problem.

The statement's "samples" are transcripts of one particular interaction, so they
cannot be fed to a program as stdin; instead this plays the game master. It
enforces the query budget of ceil(n / 2), answers each "? r" with the true
distance array, and checks the reported edge set is exactly the hidden tree.
"""
import random
from collections import deque


def tests():
    cases = [
        (2, [(1, 2)]),
        (4, [(1, 2), (2, 3), (2, 4)]),
        (5, [(4, 5), (3, 5), (2, 4), (1, 3)]),
        (6, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]),          # star at the queried root
        (6, [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)]),          # path
        (7, [(4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7)]),  # star away from the root
    ]
    rng = random.Random(17)
    for n in (3, 8, 9, 13, 30, 61):
        cases.append((n, [(rng.randint(1, v - 1), v) for v in range(2, n + 1)]))
    return cases


def distances(n, adj, root):
    dist = [-1] * (n + 1)
    dist[root] = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for nxt in adj[node]:
            if dist[nxt] < 0:
                dist[nxt] = dist[node] + 1
                queue.append(nxt)
    return dist[1:]


def interact(case, send, readline):
    n, edges = case
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    wanted = {(min(a, b), max(a, b)) for a, b in edges}

    budget = (n + 1) // 2
    used = 0
    send(str(n))
    while True:
        line = readline()
        assert line, "blank line from the program"
        parts = line.split()
        if parts[0] == "?":
            used += 1
            assert used <= budget, f"n={n}: used {used} queries, budget is {budget}"
            assert len(parts) == 2, f"malformed query {line!r}"
            root = int(parts[1])
            assert 1 <= root <= n, f"queried node {root} outside 1..{n}"
            send(" ".join(map(str, distances(n, adj, root))))
        elif parts[0] == "!":
            reported = set()
            tail = parts[1:]
            while len(reported) < n - 1:
                while len(tail) < 2:
                    try:
                        tail.extend(readline().split())
                    except AssertionError:
                        raise AssertionError(
                            f"n={n}: only {len(reported)} of {n - 1} edges were printed")
                a, b = int(tail[0]), int(tail[1])
                tail = tail[2:]
                assert 1 <= a <= n and 1 <= b <= n and a != b, f"bad edge ({a}, {b})"
                reported.add((min(a, b), max(a, b)))
            assert reported == wanted, (
                f"n={n}: reported {sorted(reported)}, the tree is {sorted(wanted)}")
            return
        else:
            raise AssertionError(f"unexpected line {line!r}")
