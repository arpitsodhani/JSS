import sys

MOD = 998244353


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        edges = [int(token) for token in data[pos:pos + 2 * m]]
        pos += 2 * m
        cases.append((n, m, edges))
    return cases


# --- clause: solve_case :: (n: int, m: int, edges: list[int]) -> int ---
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
    root = 1
    while root <= n:
        if colour[root] != -1:
            root += 1
            continue
        colour[root] = 0
        stack = [root]
        even = 1
        odd = 0
        at = 0
        while at < len(stack):
            node = stack[at]
            at += 1
            here = colour[node]
            other = here ^ 1
            for idx in range(start[node], start[node + 1]):
                nxt = adj[idx]
                seen = colour[nxt]
                if seen == here:
                    return 0
                if seen == -1:
                    colour[nxt] = other
                    if other:
                        odd += 1
                    else:
                        even += 1
                    stack.append(nxt)
        answer = answer * (pow(2, even, MOD) + pow(2, odd, MOD)) % MOD
        root += 1
    return answer


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, edges in read_input():
        out.append(str(solve_case(n, m, edges)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
