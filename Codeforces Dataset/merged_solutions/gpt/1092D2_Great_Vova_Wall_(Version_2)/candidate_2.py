# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    max_h = max(a)
    parent = list(range(n))
    size = [1] * n
    active = [False] * n
    bad = 0

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def unite(x, y):
        nonlocal bad
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if size[rx] < size[ry]:
            rx, ry = (ry, rx)
        if size[rx] & 1:
            bad -= 1
        if size[ry] & 1:
            bad -= 1
        parent[ry] = rx
        size[rx] += size[ry]
        if size[rx] & 1:
            bad += 1
    by_height = {}
    for i, h in enumerate(a):
        by_height.setdefault(h, []).append(i)
    for h in sorted(by_height):
        if h == max_h:
            break
        for i in by_height[h]:
            active[i] = True
            bad += 1
            if i > 0 and active[i - 1]:
                unite(i, i - 1)
            if i + 1 < n and active[i + 1]:
                unite(i, i + 1)
        if bad:
            print('NO')
            return
    print('YES')
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
