import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]], list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    pos = 2
    friends = []
    for _ in range(k):
        friends.append((data[pos], data[pos + 1]))
        pos += 2
    m = data[pos]
    pos += 1
    foes = []
    for _ in range(m):
        foes.append((data[pos], data[pos + 1]))
        pos += 2
    return n, friends, foes


# --- clause: largest_party :: (n: int, friends: list[tuple[int, int]], foes: list[tuple[int, int]]) -> int ---
def largest_party(n, friends, foes):
    parent = list(range(n + 1))
    for a, b in friends:
        ra = a
        while parent[ra] != ra:
            ra = parent[ra]
        rb = b
        while parent[rb] != rb:
            rb = parent[rb]
        parent[ra] = rb
    leader = [0] * (n + 1)
    for v in range(1, n + 1):
        root = v
        while parent[root] != root:
            root = parent[root]
        step = v
        while parent[step] != root:
            parent[step], step = root, parent[step]
        leader[v] = root
    counts = {}
    for v in range(1, n + 1):
        counts[leader[v]] = counts.get(leader[v], 0) + 1
    for a, b in foes:
        if leader[a] == leader[b]:
            counts[leader[a]] = 0
    best = 0
    for value in counts.values():
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    n, friends, foes = read_input()
    sys.stdout.write(str(largest_party(n, friends, foes)) + "\n")


if __name__ == "__main__":
    main()
