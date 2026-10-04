import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        x = data[1 + 2 * i]
        y = data[2 + 2 * i]
        adj[x].append(y)
        adj[y].append(x)
    return n, adj


# --- clause: lay_segments :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int]] ---
def lay_segments(n, adj):
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    parent = [0] * (n + 1)
    parent[1] = 1
    stack = [(1, 0)]
    clock = 0
    while stack:
        v, state = stack.pop()
        if state == 0:
            stack.append((v, 1))
            for u in adj[v]:
                if u != parent[v]:
                    parent[u] = v
                    stack.append((u, 0))
            continue
        clock += 1
        left[v] = clock
        for u in adj[v]:
            if u == parent[v]:
                continue
            clock += 1
            right[u] = clock
    clock += 1
    right[1] = clock
    return left, right


# --- clause: main :: () -> None ---
def main():
    n, adj = read_input()
    left, right = lay_segments(n, adj)
    out = []
    for v in range(1, n + 1):
        out.append("%d %d" % (left[v], right[v]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
