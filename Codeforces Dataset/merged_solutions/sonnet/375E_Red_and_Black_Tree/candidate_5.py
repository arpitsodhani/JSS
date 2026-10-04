# CLAUSE: setup_environment
import sys

LIMIT = 10 ** 30
LOW = -10 ** 18

# CLAUSE: solve_logic
class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [LOW] * (n + 1)

    def update(self, pos, value):
        pos += 1
        while pos <= self.n:
            if value > self.bit[pos]:
                self.bit[pos] = value
            pos += pos & -pos

    def query(self, pos):
        pos += 1
        value = LOW
        while pos > 0:
            if self.bit[pos] > value:
                value = self.bit[pos]
            pos -= pos & -pos
        return value

def reduce_states(states):
    if not states:
        return {}
    needs = sorted(set(need for _, need in states.keys()))
    ids = {need: i for i, need in enumerate(needs)}
    bit = FenwickMax(len(needs))
    res = {}
    rows = sorted(((d, need, value) for (d, need), value in states.items()), key=lambda z: (z[0], z[1], -z[2]))
    for d, need, value in rows:
        pos = ids[need]
        if bit.query(pos) < value:
            res[(d, need)] = value
            bit.update(pos, value)
    return res

def insert(table, key, value):
    if value > table.get(key, LOW):
        table[key] = value

def shift_child(dp_child, edge, x):
    shifted = []
    for states in dp_child:
        table = {}
        for (dist, need), score in states.items():
            if dist == LIMIT:
                nd = LIMIT
            else:
                nd = dist + edge
                if nd > x:
                    nd = LIMIT
            if need < 0:
                nn = -1
            else:
                nn = need + edge
                if nn > x:
                    continue
            insert(table, (nd, nn), score)
        shifted.append(table)
    return shifted

def merge_layers(a, b, cap, x):
    merged = [{} for _ in range(cap + 1)]
    for ca, la in enumerate(a):
        if not la:
            continue
        for cb, lb in enumerate(b):
            total = ca + cb
            if total > cap:
                break
            if not lb:
                continue
            target = merged[total]
            for state_a, score_a in la.items():
                da, na = state_a
                for state_b, score_b in lb.items():
                    db, nb = state_b
                    nearest = da if da <= db else db
                    keep_a = na != -1 and (db == LIMIT or na + db > x)
                    keep_b = nb != -1 and (da == LIMIT or nb + da > x)
                    need_a = na if keep_a else -1
                    need_b = nb if keep_b else -1
                    need = need_a if need_a >= need_b else need_b
                    insert(target, (nearest, need), score_a + score_b)
    return [reduce_states(layer) for layer in merged]

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    x = values[1]
    colors = [0] + values[2:2 + n]
    black = sum(colors)
    graph = [[] for _ in range(n + 1)]
    pos = 2 + n
    for edge_id in range(n - 1):
        u = values[pos]
        v = values[pos + 1]
        w = values[pos + 2]
        pos += 3
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [0] * (n + 1)
    parent[1] = -1
    stack = [(1, 0)]
    order = []
    while stack:
        node, seen = stack.pop()
        if seen:
            order.append(node)
            continue
        stack.append((node, 1))
        for nxt, _ in graph[node]:
            if nxt != parent[node]:
                parent[nxt] = node
                stack.append((nxt, 0))

    dp = [None] * (n + 1)
    size = [0] * (n + 1)

    for node in order:
        layers = [{(LIMIT, 0): 0}]
        if black:
            layers.append({(0, -1): colors[node]})
        size[node] = 1
        for nxt, edge in graph[node]:
            if parent[nxt] != node:
                continue
            part = shift_child(dp[nxt], edge, x)
            layers = merge_layers(layers, part, min(black, size[node] + size[nxt]), x)
            size[node] += size[nxt]
        dp[node] = layers

    best = LOW
    if black < len(dp[1]):
        root_layer = dp[1][black]
        for key in root_layer:
            if key[1] == -1 and root_layer[key] > best:
                best = root_layer[key]
    print(-1 if best == LOW else black - best)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
