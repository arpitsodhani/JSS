import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        flat = data[pos:pos + 2 * (n - 1)]
        pos += 2 * (n - 1)
        cases.append((n, flat))
    return cases


# --- clause: build_tree :: (n: int, flat: list[int]) -> tuple[list[list[int]], list[int], list[int]] ---
def build_tree(n, flat):
    adj = [[] for _ in range(n + 1)]
    for i in range(0, len(flat), 2):
        u = flat[i]
        v = flat[i + 1]
        adj[u].append(v)
        adj[v].append(u)
    parent = [0] * (n + 1)
    order = [1]
    head = 0
    while head < len(order):
        u = order[head]
        head += 1
        for w in adj[u]:
            if w != parent[u]:
                parent[w] = u
                order.append(w)
    return adj, parent, order


# --- clause: solve_case :: (n: int, flat: list[int]) -> int ---
def solve_case(n, flat):
    adj, parent, order = build_tree(n, flat)
    size = [1] * (n + 1)
    saved = [0] * (n + 1)
    for u in reversed(order):
        kids = [w for w in adj[u] if w != parent[u]]
        if len(kids) == 1:
            saved[u] = size[kids[0]] - 1
        elif len(kids) == 2:
            first, second = kids
            cut_first = size[first] - 1 + saved[second]
            cut_second = size[second] - 1 + saved[first]
            saved[u] = cut_first if cut_first > cut_second else cut_second
        size[parent[u]] += size[u]
    return saved[1]


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, flat in read_input():
        out.append(str(solve_case(n, flat)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
