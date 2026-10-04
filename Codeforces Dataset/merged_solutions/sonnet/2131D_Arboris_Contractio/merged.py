import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        edges = []
        for _ in range(n - 1):
            edges.append((data[pos], data[pos + 1]))
            pos += 2
        cases.append((n, edges))
    return cases

# Clause fewest_moves [Confidence: 1.00]
def fewest_moves(n, edges):
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    leaves = 0
    for v in range(1, n + 1):
        if degree[v] == 1:
            leaves += 1
    near = [0] * (n + 1)
    for u, v in edges:
        if degree[v] == 1:
            near[u] += 1
        if degree[u] == 1:
            near[v] += 1
    best = leaves
    for v in range(1, n + 1):
        here = leaves - near[v]
        if degree[v] == 1:
            here -= 1
        if here < best:
            best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, edges in read_input():
        out.append(fewest_moves(n, edges))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

