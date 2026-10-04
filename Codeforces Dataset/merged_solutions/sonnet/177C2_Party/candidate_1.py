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
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a != b:
            parent[a] = b
    root_of = [0] * (n + 1)
    for v in range(1, n + 1):
        x = v
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        root_of[v] = x
    size = [0] * (n + 1)
    for v in range(1, n + 1):
        size[root_of[v]] += 1
    banned = [False] * (n + 1)
    for a, b in foes:
        if root_of[a] == root_of[b]:
            banned[root_of[a]] = True
    best = 0
    for v in range(1, n + 1):
        root = root_of[v]
        if not banned[root] and size[root] > best:
            best = size[root]
    return best


# --- clause: main :: () -> None ---
def main():
    n, friends, foes = read_input()
    sys.stdout.write(str(largest_party(n, friends, foes)) + "\n")


if __name__ == "__main__":
    main()
