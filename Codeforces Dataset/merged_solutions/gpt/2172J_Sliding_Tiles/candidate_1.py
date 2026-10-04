# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]
    h = data[1 + n:1 + n + n - 1]

    parent = list(range(n))
    left = list(range(n))
    right = list(range(n))
    cnt = [1 if x > 0 else 0 for x in a]
    start = [1] * n
    diff = [0] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def add_range(l, r, v):
        if l <= r and v:
            diff[l] += v
            diff[r + 1] -= v

    def close(root, end_y):
        root = find(root)
        c = cnt[root]
        if c > 0 and start[root] <= end_y:
            add_range(right[root] - c + 1, right[root], end_y - start[root] + 1)

    def open_component(root, start_y):
        root = find(root)
        if cnt[root] > 0:
            start[root] = start_y
        else:
            start[root] = n + 2

    def merge(x, y, end_y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return rx

        close(rx, end_y)
        close(ry, end_y)

        if left[rx] > left[ry]:
            rx, ry = ry, rx

        parent[ry] = rx
        right[rx] = right[ry]
        cnt[rx] += cnt[ry]
        open_component(rx, end_y + 1)
        return rx

    head_a = [-1] * (n + 1)
    next_a = [-1] * n
    for i, x in enumerate(a):
        if x > 0:
            next_a[i] = head_a[x]
            head_a[x] = i

    head_h = [-1] * (n + 1)
    next_h = [-1] * max(0, n - 1)
    for i, x in enumerate(h):
        if x == 0:
            merge(i, i + 1, 0)
        else:
            next_h[i] = head_h[x]
            head_h[x] = i

    for y in range(1, n + 1):
        pos = head_a[y]
        while pos != -1:
            nxt = next_a[pos]
            root = find(pos)
            close(root, y)
            cnt[root] -= 1
            open_component(root, y + 1)
            pos = nxt

        bar = head_h[y]
        while bar != -1:
            nxt = next_h[bar]
            merge(bar, bar + 1, y)
            bar = nxt

    ans = []
    cur = 0
    for i in range(n):
        cur += diff[i]
        ans.append(str(cur))

    sys.stdout.write(" ".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
