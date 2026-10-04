import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    line = sys.stdin.readline()
    while line.strip() == "":
        line = sys.stdin.readline()
    return int(line)

# Clause ask [Confidence: 1.00]
def ask(node, n):
    sys.stdout.write("? " + str(node) + "\n")
    sys.stdout.flush()
    dist = []
    while len(dist) < n:
        line = sys.stdin.readline()
        if not line:
            break
        for token in line.split():
            dist.append(int(token))
    return dist

# Clause collect_edges [Confidence: 1.00]
def collect_edges(n):
    base = ask(1, n)
    even = []
    odd = []
    for node in range(1, n + 1):
        if base[node - 1] % 2 == 0:
            even.append(node)
        else:
            odd.append(node)
    if len(even) <= (n + 1) // 2:
        side = even
    else:
        side = odd
    edges = []
    for node in side:
        if node == 1:
            dist = base
        else:
            dist = ask(node, n)
        for other in range(1, n + 1):
            if dist[other - 1] == 1:
                edges.append((node, other))
    return edges

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    edges = collect_edges(n)
    out = ["!"]
    for a, b in edges:
        out.append(str(a) + " " + str(b))
    sys.stdout.write("\n".join(out) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()

