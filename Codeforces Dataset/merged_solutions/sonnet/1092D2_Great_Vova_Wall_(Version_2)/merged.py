# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    arr = values[1:]

    groups = {}
    for idx, height in enumerate(arr):
        if height in groups:
            groups[height].append(idx)
        else:
            groups[height] = [idx]

    parent = list(range(n))
    length = [1] * n
    active = [False] * n
    odd_count = 0

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != x:
            nxt = parent[x]
            parent[x] = root
            x = nxt
        return root

    def merge(x, y):
        nonlocal odd_count
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if length[rx] < length[ry]:
            rx, ry = ry, rx
        odd_count -= length[rx] & 1
        odd_count -= length[ry] & 1
        parent[ry] = rx
        length[rx] += length[ry]
        odd_count += length[rx] & 1

    ordered = sorted(groups)
    for height in ordered[:-1]:
        for pos in groups[height]:
            active[pos] = True
            odd_count += 1
            if pos and active[pos - 1]:
                merge(pos, pos - 1)
            if pos + 1 < n and active[pos + 1]:
                merge(pos, pos + 1)
        if odd_count:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n")


# Clause finish_program [Confidence: 0.40]
main()


