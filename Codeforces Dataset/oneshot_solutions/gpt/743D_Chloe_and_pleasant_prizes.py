import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = [0] + data[1:1 + n]

    adj = [[] for _ in range(n + 1)]
    idx = 1 + n
    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    order = [1]
    parent[1] = -1

    for u in order:
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    neg_inf = -10**30
    subtree_sum = [0] * (n + 1)
    best = [neg_inf] * (n + 1)
    ans = neg_inf

    for u in reversed(order):
        total = a[u]
        current_best = neg_inf

        for v in adj[u]:
            if parent[v] == u:
                total += subtree_sum[v]
                if current_best != neg_inf:
                    ans = max(ans, current_best + best[v])
                current_best = max(current_best, best[v])

        subtree_sum[u] = total
        best[u] = max(current_best, total)

    if ans == neg_inf:
        print("Impossible")
    else:
        print(ans)

if __name__ == "__main__":
    main()
