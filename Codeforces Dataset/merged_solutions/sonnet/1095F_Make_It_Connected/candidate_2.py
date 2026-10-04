import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[tuple[int, int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    values = tokens[2:2 + n]
    offers = []
    pos = 2 + n
    for _ in range(m):
        offers.append((tokens[pos + 2], tokens[pos] - 1, tokens[pos + 1] - 1))
        pos += 3
    return n, values, offers


# --- clause: all_edges :: (n: int, values: list[int], offers: list[tuple[int, int, int]]) -> list[tuple[int, int, int]] ---
def all_edges(n, values, offers):
    cheapest = 0
    for i in range(n):
        if values[i] < values[cheapest]:
            cheapest = i
    edges = list(offers)
    for i in range(n):
        if i != cheapest:
            edges.append((values[i] + values[cheapest], i, cheapest))
    edges.sort()
    return edges


# --- clause: spanning_cost :: (n: int, edges: list[tuple[int, int, int]]) -> int ---
def spanning_cost(n, edges):
    parent = list(range(n))
    amount = 0
    joined = 0
    for weight, x, y in edges:
        a = x
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        b = y
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a == b:
            continue
        parent[a] = b
        amount += weight
        joined += 1
        if joined == n - 1:
            break
    return amount


# --- clause: main :: () -> None ---
def main():
    n, values, offers = read_input()
    edges = all_edges(n, values, offers)
    sys.stdout.write("%d\n" % spanning_cost(n, edges))


if __name__ == "__main__":
    main()
