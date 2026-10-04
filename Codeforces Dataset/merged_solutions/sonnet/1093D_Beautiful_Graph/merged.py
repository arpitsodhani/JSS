import sys
MOD = 998244353

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        edges = [int(token) for token in data[pos:pos + 2 * m]]
        pos += 2 * m
        cases.append((n, m, edges))
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(n, m, edges):
    head = [0] * (n + 1)
    for i in range(0, 2 * m, 2):
        head[edges[i]] += 1
        head[edges[i + 1]] += 1
    start = [0] * (n + 2)
    for v in range(1, n + 1):
        start[v + 1] = start[v] + head[v]
    fill = start[:]
    adj = [0] * (2 * m)
    for i in range(0, 2 * m, 2):
        u = edges[i]
        v = edges[i + 1]
        adj[fill[u]] = v
        fill[u] += 1
        adj[fill[v]] = u
        fill[v] += 1
    colour = [-1] * (n + 1)
    answer = 1
    for root in range(1, n + 1):
        if colour[root] >= 0:
            continue
        colour[root] = 0
        stack = [root]
        sides = [1, 0]
        while stack:
            node = stack.pop()
            for idx in range(start[node], start[node + 1]):
                nxt = adj[idx]
                if colour[nxt] < 0:
                    colour[nxt] = colour[node] ^ 1
                    sides[colour[nxt]] += 1
                    stack.append(nxt)
                elif colour[node] == colour[nxt]:
                    return 0
        answer = answer * (pow(2, sides[0], MOD) + pow(2, sides[1], MOD)) % MOD
    return answer

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, m, edges in read_input():
        out.append(str(solve_case(n, m, edges)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

