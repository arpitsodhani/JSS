import sys

# Clause read_input [Confidence: 1.00]
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

# Clause lay_segments [Confidence: 1.00]
def lay_segments(n, adj):
    left = [0] * (n + 1)
    high = [0] * (n + 1)
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
            high[u] = clock
    clock += 1
    high[1] = clock
    return left, high

# Clause main [Confidence: 1.00]
def main():
    n, adj = read_input()
    left, high = lay_segments(n, adj)
    out = []
    for v in range(1, n + 1):
        out.append("%d %d" % (left[v], high[v]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

