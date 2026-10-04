import sys
from array import array

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    periods = [int(x) for x in data[1:1 + n]]
    q = int(data[1 + n])
    pos = 2 + n
    queries = []
    for _ in range(q):
        kind = data[pos]
        queries.append([kind == b"C", int(data[pos + 1]), int(data[pos + 2])])
        pos += 3
    return n, periods, queries

# Clause build_tree [Confidence: 1.00]
def build_tree(n, periods):
    size = 1
    while size < n:
        size *= 2
    tree = array('i', [0]) * (2 * size * 60)
    for i in range(n):
        base = (size + i) * 60
        period = periods[i]
        for t in range(60):
            tree[base + t] = 2 if t % period == 0 else 1
    for node in range(size - 1, 0, -1):
        left = 2 * node * 60
        finish = (2 * node + 1) * 60
        here = node * 60
        for t in range(60):
            cost = tree[left + t]
            tree[here + t] = cost + tree[finish + (t + cost) % 60]
    return tree, size

# Clause set_period [Confidence: 1.00]
def set_period(tree, size, index, period):
    base = (size + index) * 60
    for t in range(60):
        tree[base + t] = 2 if t % period == 0 else 1
    node = (size + index) >> 1
    while node:
        left = 2 * node * 60
        finish = (2 * node + 1) * 60
        here = node * 60
        for t in range(60):
            cost = tree[left + t]
            tree[here + t] = cost + tree[finish + (t + cost) % 60]
        node >>= 1

# Clause travel_time [Confidence: 1.00]
def travel_time(tree, size, first, last):
    lo = first + size
    hi = last + 1 + size
    front = []
    back = []
    while lo < hi:
        if lo & 1:
            front.append(lo)
            lo += 1
        if hi & 1:
            hi -= 1
            back.append(hi)
        lo >>= 1
        hi >>= 1
    t = 0
    for node in front:
        t += tree[node * 60 + t % 60]
    for i in range(len(back) - 1, -1, -1):
        node = back[i]
        t += tree[node * 60 + t % 60]
    return t

# Clause main [Confidence: 1.00]
def main():
    n, periods, queries = read_input()
    tree, size = build_tree(n, periods)
    out = []
    for is_change, first, second in queries:
        if is_change:
            set_period(tree, size, first - 1, second)
        else:
            out.append(travel_time(tree, size, first - 1, second - 2))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

