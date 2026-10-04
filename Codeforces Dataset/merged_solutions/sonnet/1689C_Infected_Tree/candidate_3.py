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
        adj[flat[i]].append(flat[i + 1])
        adj[flat[i + 1]].append(flat[i])
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    while stack:
        u = stack.pop()
        order.append(u)
        for w in adj[u]:
            if w != parent[u]:
                parent[w] = u
                stack.append(w)
    return adj, parent, order

# --- clause: solve_case :: (n: int, flat: list[int]) -> int ---
def solve_case(n, flat):
    adj, parent, order = build_tree(n, flat)
    size = [1] * (n + 1)
    saved = [0] * (n + 1)
    for u in reversed(order):
        first = 0
        second = 0
        for w in adj[u]:
            if w == parent[u]:
                continue
            if first:
                second = w
            else:
                first = w
        if second:
            keep_first = size[first] - 1 + saved[second]
            keep_second = size[second] - 1 + saved[first]
            saved[u] = keep_first if keep_first > keep_second else keep_second
        elif first:
            saved[u] = size[first] - 1
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
