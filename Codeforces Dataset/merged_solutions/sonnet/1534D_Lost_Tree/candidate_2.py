import sys


# --- clause: read_input :: () -> int ---
def read_input():
    line = sys.stdin.readline()
    while not line.strip():
        line = sys.stdin.readline()
    return int(line.strip())


# --- clause: ask :: (node: int, n: int) -> list[int] ---
def ask(node, n):
    sys.stdout.write("? %d\n" % node)
    sys.stdout.flush()
    dist = []
    while len(dist) < n:
        line = sys.stdin.readline()
        if not line:
            break
        dist.extend(int(token) for token in line.split())
    return dist


# --- clause: collect_edges :: (n: int) -> list[tuple[int, int]] ---
def collect_edges(n):
    base = ask(1, n)
    even = []
    odd = []
    for node in range(1, n + 1):
        if base[node - 1] % 2:
            odd.append(node)
        else:
            even.append(node)
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


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    edges = collect_edges(n)
    out = ["!"]
    for a, b in edges:
        out.append("%d %d" % (a, b))
    sys.stdout.write("\n".join(out) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
