import sys


# --- clause: read_input :: () -> int ---
def read_input():
    line = sys.stdin.readline()
    while line.strip() == "":
        line = sys.stdin.readline()
    return int(line)


# --- clause: ask :: (node: int, n: int) -> list[int] ---
def ask(node, n):
    sys.stdout.write("? " + str(node) + "\n")
    sys.stdout.flush()
    dist = []
    while len(dist) < n:
        line = sys.stdin.readline()
        if not line:
            break
        tokens = line.split()
        dist += [int(token) for token in tokens]
    return dist


# --- clause: collect_edges :: (n: int) -> list[tuple[int, int]] ---
def collect_edges(n):
    base = ask(1, n)
    odd = []
    even = []
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
        dist = base if node == 1 else ask(node, n)
        for other in range(1, n + 1):
            if dist[other - 1] == 1:
                edges.append((node, other))
    return edges


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    edges = collect_edges(n)
    out = ["!"]
    for edge in edges:
        out.append(str(edge[0]) + " " + str(edge[1]))
    sys.stdout.write("\n".join(out) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
