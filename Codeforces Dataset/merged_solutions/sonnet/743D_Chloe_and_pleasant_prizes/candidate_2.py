import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [0] + [int(token) for token in data[1:n + 1]]
    adj = [[] for _ in range(n + 1)]
    idx = n + 1
    for _ in range(n - 1):
        a, b = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[a].append(b)
        adj[b].append(a)
    return n, values, adj


# --- clause: build_order :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int]] ---
def build_order(n, adj):
    parent = [0] * (n + 1)
    seen = [False] * (n + 1)
    order = []
    stack = [1]
    seen[1] = True
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbour in adj[node]:
            if seen[neighbour]:
                continue
            seen[neighbour] = True
            parent[neighbour] = node
            stack.append(neighbour)
    return order, parent


# --- clause: compute_answer :: (n: int, values: list[int], order: list[int], parent: list[int]) -> int | None ---
def compute_answer(n, values, order, parent):
    floor = -(1 << 62)
    total = list(values)
    best = [floor] * (n + 1)
    top1 = [floor] * (n + 1)
    top2 = [floor] * (n + 1)
    for node in reversed(order):
        reach = total[node]
        if best[node] > reach:
            reach = best[node]
        best[node] = reach
        up = parent[node]
        if up != 0:
            total[up] += total[node]
            if top1[up] < reach:
                top2[up] = top1[up]
                top1[up] = reach
            elif top2[up] < reach:
                top2[up] = reach
            if best[up] < reach:
                best[up] = reach
    answer = None
    for node in range(1, n + 1):
        if top2[node] > floor:
            pair = top1[node] + top2[node]
            if answer is None or answer < pair:
                answer = pair
    return answer


# --- clause: main :: () -> None ---
def main():
    n, values, adj = read_input()
    order, parent = build_order(n, adj)
    answer = compute_answer(n, values, order, parent)
    if answer is None:
        sys.stdout.write("Impossible\n")
    else:
        sys.stdout.write("%d\n" % answer)


if __name__ == "__main__":
    main()
