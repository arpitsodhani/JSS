# CLAUSE: setup_environment
import sys

MINUS = -10 ** 25

# CLAUSE: solve_logic
def base_time(numbers):
    ordered = sorted(numbers, reverse=True)
    res = len(ordered)
    index = 0
    for number in ordered:
        if number + index > res:
            res = number + index
        index += 1
    return res

def local_time(entries):
    length = len(entries)
    if length == 0:
        return 0
    ans = base_time([x for x, y in entries])
    for banned in range(length):
        numbers = []
        for i in range(length):
            if i != banned:
                numbers.append(entries[i][0])
        now = base_time(numbers)
        if entries[banned][1] > now:
            now = entries[banned][1]
        if now < ans:
            ans = now
    return ans

def orient(entries):
    degree = len(entries)
    if degree == 1:
        return [0]
    ids = sorted(range(degree), key=lambda i: (-entries[i][0], i))
    position = [0] * degree
    cost = [0] * degree
    tail = [0] * degree
    for place, old in enumerate(ids):
        position[old] = place
        cost[place], tail[place] = entries[old]
    v0 = []
    v1 = []
    v2 = []
    for i, item in enumerate(cost):
        v0.append(item + i)
        v1.append(item + i - 1)
        v2.append(item + i - 2)
    pre = [[0] * degree for _ in range(3)]
    for i in range(degree):
        pre[0][i] = v0[i] if i == 0 else max(pre[0][i - 1], v0[i])
        pre[1][i] = v1[i] if i == 0 else max(pre[1][i - 1], v1[i])
        pre[2][i] = v2[i] if i == 0 else max(pre[2][i - 1], v2[i])
    suf = [[0] * degree for _ in range(3)]
    for i in range(degree - 1, -1, -1):
        suf[0][i] = v0[i] if i + 1 == degree else max(suf[0][i + 1], v0[i])
        suf[1][i] = v1[i] if i + 1 == degree else max(suf[1][i + 1], v1[i])
        suf[2][i] = v2[i] if i + 1 == degree else max(suf[2][i + 1], v2[i])
    def one(a):
        res = degree - 1
        if a:
            res = max(res, pre[0][a - 1])
        if a + 1 < degree:
            res = max(res, suf[1][a + 1])
        return res
    def two(a, b):
        if b < a:
            a, b = b, a
        res = degree - 2
        if a:
            res = max(res, pre[0][a - 1])
        if a + 1 < b:
            inside = MINUS
            j = a + 1
            while j < b:
                if v1[j] > inside:
                    inside = v1[j]
                j += 1
            res = max(res, inside)
        if b + 1 < degree:
            res = max(res, suf[2][b + 1])
        return res
    by_pos = []
    for blocked in range(degree):
        best = one(blocked)
        nxt = 0
        while nxt < degree:
            if nxt != blocked:
                value = two(blocked, nxt)
                value = max(value, tail[nxt])
                if value < best:
                    best = value
            nxt += 1
        by_pos.append(best)
    result = [0] * degree
    for i in range(degree):
        result[i] = by_pos[position[i]]
    return result

def run():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    if n == 1:
        print(0)
        return
    parent = [-2] * n
    parent[0] = -1
    order = []
    stack = [0]
    while stack:
        v = stack.pop()
        order.append(v)
        for u in adj[v]:
            if parent[u] == -2:
                parent[u] = v
                stack.append(u)
    down_c = {}
    down_d = {}
    for v in reversed(order):
        if v == 0:
            continue
        pieces = []
        for u in adj[v]:
            if parent[u] == v:
                pieces.append((down_c[(u, v)], down_d[(u, v)]))
        got = local_time(pieces)
        p = parent[v]
        down_d[(v, p)] = got
        down_c[(v, p)] = got + 1
    for v in order:
        pieces = []
        ok = True
        for u in adj[v]:
            key = (u, v)
            if key not in down_c:
                ok = False
                break
            pieces.append((down_c[key], down_d[key]))
        if ok:
            values = orient(pieces)
            for u, value in zip(adj[v], values):
                down_d[(v, u)] = value
                down_c[(v, u)] = value + 1
    answer = 0
    for v, nei in enumerate(adj):
        numbers = [down_c[(u, v)] for u in nei]
        numbers.sort(reverse=True)
        cur = len(numbers)
        if len(numbers) >= 1:
            cur = max(cur, len(numbers) - 1 + numbers[0])
        i = 1
        while i < len(numbers):
            cur = max(cur, numbers[0] + numbers[i] + i - 1)
            i += 1
        if cur > answer:
            answer = cur
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    run()
