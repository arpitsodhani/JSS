# CLAUSE: setup_environment
import sys
from collections import Counter, defaultdict

# CLAUSE: solve_logic
def normalized_edges(a, b, c):
    return [
        (a, b) if a < b else (b, a),
        (b, c) if b < c else (c, b),
        (a, c) if a < c else (c, a),
    ]

def solve_case(n, triangles):
    if n == 3:
        return triangles[0]

    counts = Counter()
    for a, b, c in triangles:
        counts.update(normalized_edges(a, b, c))

    graph = defaultdict(list)
    for (u, v), amount in counts.items():
        if amount == 1:
            graph[u].append(v)
            graph[v].append(u)

    first = next(iter(graph))
    second = graph[first][0]
    path = [first, second]

    while path[-1] != first:
        previous = path[-2]
        current = path[-1]
        choices = graph[current]
        path.append(choices[0] if choices[0] != previous else choices[1])

    return path[:-1]

# CLAUSE: finish_program
def main():
    values = sys.stdin.buffer.read().split()
    at = 0
    t = int(values[at])
    at += 1
    output = []

    for _ in range(t):
        n = int(values[at])
        at += 1
        triangles = []
        for _ in range(n - 2):
            triangles.append((int(values[at]), int(values[at + 1]), int(values[at + 2])))
            at += 3
        output.append(" ".join(str(x) for x in solve_case(n, triangles)))

    sys.stdout.write("\n".join(output))

main()
