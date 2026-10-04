# CLAUSE: setup_environment
import sys
from collections import deque

INF = 10 ** 30
NEG = -10 ** 18

# CLAUSE: solve_logic
def prune_layer(layer):
    if len(layer) <= 1:
        return layer
    all_needs = sorted(set(k[1] for k in layer))
    index = {v: i for i, v in enumerate(all_needs)}
    tree = [NEG] * (len(all_needs) + 1)
    ans = {}
    records = []
    for key, val in layer.items():
        records.append((key[0], key[1], val))
    records.sort(key=lambda x: (x[0], x[1], -x[2]))
    for d, need, value in records:
        i = index[need] + 1
        mx = NEG
        j = i
        while j > 0:
            if tree[j] > mx:
                mx = tree[j]
            j -= j & -j
        if mx >= value:
            continue
        ans[(d, need)] = value
        j = i
        while j <= len(all_needs):
            if value > tree[j]:
                tree[j] = value
            j += j & -j
    return ans

def add_state(bucket, d, need, value):
    key = (d, need)
    if value > bucket.get(key, NEG):
        bucket[key] = value

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    data = [int(x) for x in raw]
    n = data[0]
    x = data[1]
    colors = [0] + data[2:2 + n]
    total = sum(colors)
    adj = [[] for _ in range(n + 1)]
    at = 2 + n
    for _ in range(n - 1):
        a = data[at]
        b = data[at + 1]
        c = data[at + 2]
        at += 3
        adj[a].append((b, c))
        adj[b].append((a, c))

    parent = [0] * (n + 1)
    parent[1] = -1
    order = []
    q = deque([1])
    while q:
        v = q.popleft()
        order.append(v)
        for to, _ in adj[v]:
            if to != parent[v]:
                parent[to] = v
                q.append(to)

    dp = [None] * (n + 1)
    size = [0] * (n + 1)

    for v in reversed(order):
        layers = [{(INF, 0): 0}]
        if total > 0:
            layers.append({(0, -1): colors[v]})
        size[v] = 1

        children = []
        for to, w in adj[v]:
            if parent[to] == v:
                children.append((to, w))

        for child, length in children:
            moved = []
            for layer in dp[child]:
                now = {}
                for (d, need), score in layer.items():
                    if d == INF or d + length > x:
                        nd = INF
                    else:
                        nd = d + length
                    if need == -1:
                        nn = -1
                    else:
                        nn = need + length
                        if nn > x:
                            continue
                    add_state(now, nd, nn, score)
                moved.append(now)

            bound = min(total, size[v] + size[child])
            merged = [{} for _ in range(bound + 1)]
            for left_count in range(len(layers)):
                left = layers[left_count]
                if not left:
                    continue
                right_limit = min(len(moved), bound - left_count + 1)
                for right_count in range(right_limit):
                    right = moved[right_count]
                    if not right:
                        continue
                    place = merged[left_count + right_count]
                    for (d1, n1), s1 in left.items():
                        for (d2, n2), s2 in right.items():
                            nearest = min(d1, d2)
                            a = -1
                            b = -1
                            if n1 != -1 and (d2 == INF or n1 + d2 > x):
                                a = n1
                            if n2 != -1 and (d1 == INF or n2 + d1 > x):
                                b = n2
                            add_state(place, nearest, max(a, b), s1 + s2)
            layers = [prune_layer(layer) for layer in merged]
            size[v] += size[child]
        dp[v] = layers

    best = NEG
    if total < len(dp[1]):
        for (d, need), value in dp[1][total].items():
            if need == -1:
                best = max(best, value)
    sys.stdout.write(str(-1 if best == NEG else total - best))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
