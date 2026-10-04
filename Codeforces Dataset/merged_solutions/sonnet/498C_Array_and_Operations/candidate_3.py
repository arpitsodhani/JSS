import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    values = [int(token) for token in data[2:2 + n]]
    pairs = [int(token) for token in data[2 + n:2 + n + 2 * m]]
    return n, m, values, pairs


# --- clause: prime_powers :: (n: int, values: list[int]) -> dict ---
def prime_powers(n, values):
    table = {}
    for i in range(n):
        rest = values[i]
        factor = 2
        while factor * factor <= rest:
            if rest % factor == 0:
                count = 0
                while rest % factor == 0:
                    rest //= factor
                    count += 1
                table.setdefault(factor, [0] * n)[i] = count
            factor += 1
        if rest > 1:
            table.setdefault(rest, [0] * n)[i] = 1
    return table


# --- clause: max_flow :: (n: int, m: int, pairs: list[int], caps: list[int]) -> int ---
def max_flow(n, m, pairs, caps):
    nodes = n + 2
    source = n
    sink = n + 1
    graph = [[0] * nodes for _ in range(nodes)]
    for i in range(n):
        if i % 2 == 0:
            graph[source][i] = caps[i]
        else:
            graph[i][sink] = caps[i]
    for k in range(m):
        u = pairs[2 * k] - 1
        v = pairs[2 * k + 1] - 1
        if u % 2:
            u, v = v, u
        graph[u][v] = 1 << 30
    total = 0
    while True:
        parent = [-1] * nodes
        parent[source] = source
        stack = [source]
        while stack and parent[sink] < 0:
            node = stack.pop()
            for nxt in range(nodes):
                if parent[nxt] < 0 and graph[node][nxt] > 0:
                    parent[nxt] = node
                    stack.append(nxt)
        if parent[sink] < 0:
            return total
        push = 1 << 60
        node = sink
        while node != source:
            up = parent[node]
            if graph[up][node] < push:
                push = graph[up][node]
            node = up
        node = sink
        while node != source:
            up = parent[node]
            graph[up][node] -= push
            graph[node][up] += push
            node = up
        total += push


# --- clause: main :: () -> None ---
def main():
    n, m, values, pairs = read_input()
    table = prime_powers(n, values)
    answer = 0
    for caps in table.values():
        answer += max_flow(n, m, pairs, caps)
    print(answer)


if __name__ == "__main__":
    main()
