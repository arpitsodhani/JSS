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
        if line == "":
            break
        parts = line.split()
        for token in parts:
            dist.append(int(token))
    return dist


# --- clause: collect_edges :: (n: int) -> list[tuple[int, int]] ---
def collect_edges(n):
    base = ask(1, n)
    even = []
    odd = []
    for node in range(1, n + 1):
        if base[node - 1] % 2 == 0:
            even.append(node)
        else:
            odd.append(node)
    budget = (n + 1) // 2
    side = even if len(even) <= budget else odd
    edges = []
    for node in side:
        if node == 1:
            dist = base
        else:
            dist = ask(node, n)
        for other in range(1, n + 1):
            if dist[other - 1] != 1:
                continue
            edges.append((node, other))
    return edges


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    edges = collect_edges(n)
    out = ["!"]
    for a, b in edges:
        out.append(str(a) + " " + str(b))
    print("\n".join(out))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
