import sys
from array import array


# --- clause: read_input :: () -> tuple[int, list[int], list[list[int]]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    periods = [int(x) for x in raw[1:1 + n]]
    q = int(raw[1 + n])
    offset = 2 + n
    queries = []
    for _ in range(q):
        kind = raw[offset]
        queries.append([kind == b"C", int(raw[offset + 1]), int(raw[offset + 2])])
        offset += 3
    return n, periods, queries


# --- clause: build_tree :: (n: int, periods: list[int]) -> tuple[array, int] ---
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
        second_side = (2 * node + 1) * 60
        here = node * 60
        for t in range(60):
            cost = tree[left + t]
            tree[here + t] = cost + tree[second_side + (t + cost) % 60]
    return tree, size


# --- clause: set_period :: (tree: array, size: int, index: int, period: int) -> None ---
def set_period(tree, size, index, period):
    base = (size + index) * 60
    for t in range(60):
        tree[base + t] = 2 if t % period == 0 else 1
    node = (size + index) >> 1
    while node:
        left = 2 * node * 60
        second_side = (2 * node + 1) * 60
        here = node * 60
        for t in range(60):
            cost = tree[left + t]
            tree[here + t] = cost + tree[second_side + (t + cost) % 60]
        node >>= 1


# --- clause: travel_time :: (tree: array, size: int, first: int, last: int) -> int ---
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


# --- clause: main :: () -> None ---
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
