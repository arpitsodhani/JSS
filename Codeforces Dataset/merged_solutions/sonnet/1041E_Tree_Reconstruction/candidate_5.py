# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def fail():
    sys.stdout.write("NO\n")

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return
    n = raw[0]
    limits = []
    seen = [0] * (n + 1)

    for i in range(1, len(raw), 2):
        u = raw[i]
        v = raw[i + 1]
        if u != n and v != n:
            fail()
            return
        leaf = v if u == n else u
        if leaf == n:
            fail()
            return
        if seen[leaf] == 0:
            limits.append(leaf)
        seen[leaf] += 1

    limits.sort()
    in_limits = [False] * (n + 1)
    for value in limits:
        in_limits[value] = True

    unused = deque()
    for value in range(1, n):
        if not in_limits[value]:
            unused.append(value)

    tree_edges = []
    attach = []

    for limit in limits:
        path = []
        extra = seen[limit] - 1
        while extra:
            if not unused or unused[0] > limit:
                fail()
                return
            path.append(unused.popleft())
            extra -= 1
        path.append(limit)
        attach.append(path[0])
        i = 0
        while i + 1 < len(path):
            tree_edges.append((path[i], path[i + 1]))
            i += 1

    for vertex in attach:
        tree_edges.append((n, vertex))

    if len(tree_edges) != n - 1:
        fail()
        return

    output = ["YES"]
    for u, v in tree_edges:
        output.append(f"{u} {v}")
    sys.stdout.write("\n".join(output))
    sys.stdout.write("\n")

# CLAUSE: finish_program
main()
