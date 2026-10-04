# CLAUSE: setup_environment
import sys
from bisect import bisect_right
from collections import deque

BIG = 10 ** 40

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    cards = []
    p = 1
    for i in range(1, n + 1):
        a, b, c, d = values[p], values[p + 1], values[p + 2], values[p + 3]
        p += 4
        cards.append((a, b, c, d, i))

    order = sorted(range(n), key=lambda z: cards[z][0])
    axes = [cards[z][0] for z in order]
    size = 1
    while size < n:
        size <<= 1

    seg = [BIG] * (size << 1)
    for pos, idx in enumerate(order):
        seg[size + pos] = cards[idx][1]
    for pos in range(size - 1, 0, -1):
        left = seg[pos << 1]
        right = seg[pos << 1 | 1]
        seg[pos] = left if left < right else right

    def erase(pos):
        pos += size
        seg[pos] = BIG
        pos >>= 1
        while pos:
            left = seg[pos << 1]
            right = seg[pos << 1 | 1]
            seg[pos] = left if left < right else right
            pos >>= 1

    def first_ok(limit, y):
        if limit < 0 or seg[1] > y:
            return -1
        node = 1
        left = 0
        right = size - 1
        while left != right:
            mid = (left + right) >> 1
            child = node << 1
            if left <= limit and seg[child] <= y:
                node = child
                right = mid
            else:
                node = child | 1
                left = mid + 1
        if left <= limit and left < n and seg[node] <= y:
            return left
        return -1

    parent = [-1] * (n + 1)
    dist = [-1] * (n + 1)
    q = deque()

    def expand(x, y, prev):
        upto = bisect_right(axes, x) - 1
        while True:
            pos = first_ok(upto, y)
            if pos < 0:
                break
            idx = order[pos]
            card_id = cards[idx][4]
            parent[card_id] = prev
            dist[card_id] = 1 if prev == 0 else dist[prev] + 1
            q.append(card_id)
            erase(pos)

    expand(0, 0, 0)
    while q and dist[n] < 0:
        v = q.popleft()
        expand(cards[v - 1][2], cards[v - 1][3], v)

    if dist[n] < 0:
        sys.stdout.write("-1\n")
        return

    route = []
    cur = n
    while cur:
        route.append(cur)
        cur = parent[cur]
    route.reverse()
    sys.stdout.write(str(len(route)) + "\n" + " ".join(map(str, route)) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
