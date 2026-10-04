# CLAUSE: setup_environment
import sys
from bisect import bisect_right

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    cards = []
    p = 1
    for i in range(1, n + 1):
        a, b, c, d = (data[p], data[p + 1], data[p + 2], data[p + 3])
        p += 4
        cards.append((a, b, c, d, i))
    order = sorted(range(n), key=lambda k: cards[k][0])
    sorted_a = [cards[k][0] for k in order]
    size = 1
    while size < n:
        size <<= 1
    inf = 10 ** 30
    seg = [inf] * (2 * size)
    for pos, idx in enumerate(order):
        seg[size + pos] = cards[idx][1]
    for i in range(size - 1, 0, -1):
        seg[i] = min(seg[i << 1], seg[i << 1 | 1])
    parent = [-2] * (n + 1)
    parent[0] = -1
    queue = [0]
    head = 0
    found = False
    cx = [0] * (n + 1)
    cy = [0] * (n + 1)
    for a, b, c, d, idx in cards:
        cx[idx] = c
        cy[idx] = d

    def remove(pos):
        node = size + pos
        seg[node] = inf
        node >>= 1
        while node:
            val = min(seg[node << 1], seg[node << 1 | 1])
            if seg[node] == val:
                seg[node] = val
            else:
                seg[node] = val
            node >>= 1

    def find_first(node, left, right, ql, qr, y):
        if qr <= left or right <= ql or seg[node] > y:
            return -1
        if right - left == 1:
            return left
        mid = left + right >> 1
        res = find_first(node << 1, left, mid, ql, qr, y)
        if res != -1:
            return res
        return find_first(node << 1 | 1, mid, right, ql, qr, y)
    while head < len(queue) and (not found):
        v = queue[head]
        head += 1
        x, y = (cx[v], cy[v])
        limit = bisect_right(sorted_a, x)
        while limit > 0 and seg[1] <= y:
            pos = find_first(1, 0, size, 0, limit, y)
            if pos == -1 or pos >= n:
                break
            idx = order[pos]
            card_id = cards[idx][4]
            if parent[card_id] == -2:
                parent[card_id] = v
                if card_id == n:
                    found = True
                    break
                queue.append(card_id)
            remove(pos)
    if parent[n] == -2:
        print(-1)
        return
    ans = []
    cur = n
    while cur != 0:
        ans.append(cur)
        cur = parent[cur]
    ans.reverse()
    print(len(ans))
    print(*ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
