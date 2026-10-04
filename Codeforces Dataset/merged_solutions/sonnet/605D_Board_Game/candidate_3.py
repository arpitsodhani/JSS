# CLAUSE: setup_environment
import sys
from bisect import bisect_right
from collections import deque

INF = 10 ** 35

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    raw = [None] * (n + 1)
    k = 1
    for card in range(1, n + 1):
        raw[card] = (data[k], data[k + 1], data[k + 2], data[k + 3])
        k += 4

    by_b = list(range(1, n + 1))
    by_b.sort(key=lambda card: raw[card][1])
    sorted_b = [raw[card][1] for card in by_b]

    base = 1
    while base < n:
        base <<= 1
    tree = [INF] * (base * 2)

    for i, card in enumerate(by_b):
        tree[base + i] = raw[card][0]
    for i in range(base - 1, 0, -1):
        tree[i] = min(tree[i << 1], tree[i << 1 | 1])

    def drop(i):
        i += base
        tree[i] = INF
        while i > 1:
            i >>= 1
            tree[i] = min(tree[i << 1], tree[i << 1 | 1])

    def locate(limit, x):
        if limit < 0 or tree[1] > x:
            return -1
        stack = [(1, 0, base - 1)]
        while stack:
            node, left, right = stack.pop()
            if left > limit or tree[node] > x:
                continue
            if left == right:
                return left if left < n else -1
            mid = (left + right) >> 1
            stack.append((node << 1 | 1, mid + 1, right))
            stack.append((node << 1, left, mid))
        return -1

    previous = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    queue = deque()

    def take_all(x, y, source):
        limit = bisect_right(sorted_b, y) - 1
        found = locate(limit, x)
        while found != -1:
            card = by_b[found]
            previous[card] = source
            depth[card] = 1 if source == 0 else depth[source] + 1
            queue.append(card)
            drop(found)
            found = locate(limit, x)

    take_all(0, 0, 0)
    while queue:
        current = queue.popleft()
        if current == n:
            break
        take_all(raw[current][2], raw[current][3], current)

    if depth[n] == -1:
        print(-1)
    else:
        ans = []
        node = n
        while node:
            ans.append(node)
            node = previous[node]
        ans.reverse()
        print(len(ans))
        print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
