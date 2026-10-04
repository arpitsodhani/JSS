import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    offset = 2
    known = []
    for _ in range(n):
        hits = raw[offset]
        offset += 1
        known.append(raw[offset:offset + hits])
        offset += hits
    return m, known


# --- clause: find_root :: (parent: list[int], node: int) -> int ---
def find_root(parent, node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node


# --- clause: least_cost :: (m: int, known: list[list[int]]) -> int ---
def least_cost(m, known):
    n = len(known)
    parent = [i for i in range(n + m + 1)]
    speaks = False
    for i in range(n):
        for language in known[i]:
            speaks = True
            a = find_root(parent, i)
            b = find_root(parent, n + language)
            if a != b:
                parent[a] = b
    groups = set()
    for i in range(n):
        groups.add(find_root(parent, i))
    if not speaks:
        return n
    return len(groups) - 1


# --- clause: main :: () -> None ---
def main():
    m, known = read_input()
    sys.stdout.write("%d\n" % least_cost(m, known))


if __name__ == "__main__":
    main()
