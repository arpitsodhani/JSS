import sys


# --- clause: read_input :: () -> list[tuple[int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        s = data[pos]
        pos += 1
        a = data[pos]
        pos += 1
        cases.append((n, s, a))
    return cases


# --- clause: find_root :: (parent: list[int], parity: list[int], x: int) -> tuple[int, int] ---
def find_root(parent, parity, x):
    root = x
    acc = 0
    while parent[root] != root:
        acc ^= parity[root]
        root = parent[root]
    node = x
    rel = acc
    while parent[node] != node:
        nxt = parent[node]
        nxt_rel = rel ^ parity[node]
        parent[node] = root
        parity[node] = rel
        node = nxt
        rel = nxt_rel
    return root, acc


# --- clause: solve_case :: (n: int, s: bytes, a: bytes) -> int ---
def solve_case(n, s, a):
    parent = list(range(n))
    parity = [0] * n
    need_open = [False] * n
    need_close = [False] * n
    for i in range(n - 3):
        if a[i] != 49:
            continue
        need_open[i] = True
        need_close[i + 3] = True
        left, pl = find_root(parent, parity, i + 1)
        right, pr = find_root(parent, parity, i + 2)
        if left == right:
            if pl == pr:
                return -1
        else:
            parent[left] = right
            parity[left] = pl ^ pr ^ 1
    fixed = [-1] * n
    for i in range(n):
        if need_open[i] and need_close[i]:
            return -1
        if need_open[i]:
            want = 0
        elif need_close[i]:
            want = 1
        else:
            continue
        root, rel = find_root(parent, parity, i)
        value = want ^ rel
        if fixed[root] < 0:
            fixed[root] = value
        elif fixed[root] != value:
            return -1
    cost_open = [0] * n
    cost_close = [0] * n
    for i in range(n):
        root, rel = find_root(parent, parity, i)
        current = 1
        if s[i] == 40:
            current = 0
        if rel != current:
            cost_open[root] += 1
        if rel == current:
            cost_close[root] += 1
    total = 0
    for root in range(n):
        if parent[root] != root:
            continue
        if fixed[root] == 0:
            total += cost_open[root]
        elif fixed[root] == 1:
            total += cost_close[root]
        elif cost_open[root] < cost_close[root]:
            total += cost_open[root]
        else:
            total += cost_close[root]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
