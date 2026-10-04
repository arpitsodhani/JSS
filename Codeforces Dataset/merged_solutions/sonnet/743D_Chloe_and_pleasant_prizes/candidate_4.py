import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [0] * (n + 1)
    for i in range(n):
        values[i + 1] = int(data[i + 1])
    adj = [[] for _ in range(n + 1)]
    pos = n + 1
    for _ in range(n - 1):
        u = int(data[pos])
        v = int(data[pos + 1])
        pos += 2
        adj[v].append(u)
        adj[u].append(v)
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
        for nxt in adj[node]:
            if not seen[nxt]:
                stack.append(nxt)
                seen[nxt] = True
                parent[nxt] = node
    return order, parent


# --- clause: compute_answer :: (n: int, values: list[int], order: list[int], parent: list[int]) -> int | None ---
def compute_answer(n, values, order, parent):
    floor = -(1 << 62)
    total = values[:]
    best = [floor] * (n + 1)
    top1 = [floor] * (n + 1)
    top2 = [floor] * (n + 1)
    for node in reversed(order):
        reach = total[node]
        if reach < best[node]:
            reach = best[node]
        best[node] = reach
        up = parent[node]
        if up:
            total[up] = total[up] + total[node]
            if reach > top1[up]:
                top2[up] = top1[up]
                top1[up] = reach
            elif reach > top2[up]:
                top2[up] = reach
            if reach > best[up]:
                best[up] = reach
    answer = None
    for node in range(n, 0, -1):
        if top2[node] > floor:
            pair = top1[node] + top2[node]
            if answer is None or pair > answer:
                answer = pair
    return answer


# --- clause: main :: () -> None ---
def main():
    n, values, adj = read_input()
    order, parent = build_order(n, adj)
    result = compute_answer(n, values, order, parent)
    if result is None:
        sys.stdout.write("Impossible\n")
    else:
        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    main()
