# CLAUSE: setup_environment
import sys
from bisect import bisect_right

EMPTY = 10 ** 32

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    d = [0] * (n + 1)

    p = 1
    for i in range(1, n + 1):
        a[i] = data[p]
        b[i] = data[p + 1]
        c[i] = data[p + 2]
        d[i] = data[p + 3]
        p += 4

    order = list(range(1, n + 1))
    order.sort(key=a.__getitem__)
    sorted_a = [a[i] for i in order]

    size = 1
    while size < n:
        size <<= 1

    minimum_b = [EMPTY] * (2 * size)
    for pos in range(n):
        minimum_b[size + pos] = b[order[pos]]
    for pos in range(size - 1, 0, -1):
        minimum_b[pos] = min(minimum_b[pos + pos], minimum_b[pos + pos + 1])

    def disable(pos):
        pos += size
        minimum_b[pos] = EMPTY
        pos >>= 1
        while pos:
            minimum_b[pos] = min(minimum_b[pos + pos], minimum_b[pos + pos + 1])
            pos >>= 1

    def scan(pos, left, right, limit, y):
        if left > limit or minimum_b[pos] > y:
            return -1
        if left == right:
            return left if left < n else -1
        mid = (left + right) >> 1
        found = scan(pos + pos, left, mid, limit, y)
        if found != -1:
            return found
        return scan(pos + pos + 1, mid + 1, right, limit, y)

    parent = [-1] * (n + 1)
    level = [-1] * (n + 1)
    q = [0]
    head = 0
    state_x = [0]
    state_y = [0]

    while head < len(q) and level[n] == -1:
        source = q[head]
        x = state_x[head]
        y = state_y[head]
        head += 1
        limit = bisect_right(sorted_a, x) - 1
        while limit >= 0 and minimum_b[1] <= y:
            pos = scan(1, 0, size - 1, limit, y)
            if pos == -1:
                break
            card = order[pos]
            parent[card] = source
            level[card] = 1 if source == 0 else level[source] + 1
            q.append(card)
            state_x.append(c[card])
            state_y.append(d[card])
            disable(pos)

    if level[n] == -1:
        sys.stdout.write("-1\n")
        return

    answer = []
    cur = n
    while cur != 0:
        answer.append(cur)
        cur = parent[cur]
    answer.reverse()
    sys.stdout.write(str(len(answer)) + "\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
