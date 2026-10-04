import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    reader = 2
    known = []
    for _ in range(n):
        seen_count = data[reader]
        reader += 1
        known.append(data[reader:reader + seen_count])
        reader += seen_count
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
    speakers = [[] for _ in range(m + 1)]
    for i in range(n):
        for language in known[i]:
            speakers[language].append(i)
    alone = True
    for language in range(1, m + 1):
        crowd = speakers[language]
        if crowd:
            alone = False
        for j in range(1, len(crowd)):
            a = find_root(parent, crowd[0])
            b = find_root(parent, crowd[j])
            if a != b:
                parent[a] = b
    if alone:
        return n
    groups = 0
    for i in range(n):
        if find_root(parent, i) == i:
            groups += 1
    return groups - 1


# --- clause: main :: () -> None ---
def main():
    m, known = read_input()
    sys.stdout.write("%d\n" % least_cost(m, known))


if __name__ == "__main__":
    main()
