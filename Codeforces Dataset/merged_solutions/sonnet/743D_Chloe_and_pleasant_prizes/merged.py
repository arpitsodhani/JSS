import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [0] * (n + 1)
    for i in range(1, n + 1):
        values[i] = int(data[i])
    adj = [[] for _ in range(n + 1)]
    pos = n + 1
    for _ in range(n - 1):
        u = int(data[pos])
        v = int(data[pos + 1])
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, values, adj

# Clause build_order [Confidence: 1.00]
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
                seen[nxt] = True
                parent[nxt] = node
                stack.append(nxt)
    return order, parent

# Clause compute_answer [Confidence: 1.00]
def compute_answer(n, values, order, parent):
    floor = -(1 << 62)
    total = values[:]
    best = [floor] * (n + 1)
    top1 = [floor] * (n + 1)
    top2 = [floor] * (n + 1)
    for node in reversed(order):
        reach = total[node]
        if best[node] > reach:
            reach = best[node]
        best[node] = reach
        up = parent[node]
        if up:
            total[up] += total[node]
            if reach > top1[up]:
                top2[up] = top1[up]
                top1[up] = reach
            elif reach > top2[up]:
                top2[up] = reach
            if reach > best[up]:
                best[up] = reach
    answer = None
    for node in range(1, n + 1):
        if top2[node] > floor:
            pair = top1[node] + top2[node]
            if answer is None or pair > answer:
                answer = pair
    return answer

# Clause main [Confidence: 1.00]
def main():
    n, values, adj = read_input()
    order, parent = build_order(n, adj)
    answer = compute_answer(n, values, order, parent)
    if answer is None:
        sys.stdout.write("Impossible\n")
    else:
        sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()

