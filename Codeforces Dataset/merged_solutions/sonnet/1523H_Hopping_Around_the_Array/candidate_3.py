# CLAUSE: setup_environment
import sys
from array import array

def sparse_layers(rows, n):
    layers = [rows]
    span = 1
    while span * 2 <= n:
        prev = layers[-1]
        nxt = []
        limit = n - span * 2 + 1
        for row in prev:
            cur = array('i', [0]) * limit
            for i in range(limit):
                a = row[i]
                b = row[i + span]
                cur[i] = a if a >= b else b
            nxt.append(cur)
        layers.append(nxt)
        span *= 2
    return layers

def rmq(st, logs, budget, left, right):
    if right < left:
        return left
    p = logs[right - left + 1]
    row = st[p][budget]
    other = right - (1 << p) + 1
    a = row[left]
    b = row[other]
    return a if a >= b else b

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return
    n, q = raw[0], raw[1]
    pos = 2
    arr = raw[pos:pos + n]
    pos += n

    packed = []
    max_budget = 0
    for order in range(q):
        l = raw[pos] - 1
        r = raw[pos + 1] - 1
        k = raw[pos + 2]
        pos += 3
        packed.append((l, r, k, order))
        if k > max_budget:
            max_budget = k

    logs = [0] * (n + 1)
    for value in range(2, n + 1):
        logs[value] = logs[value >> 1] + 1

    levels_count = (n + 1).bit_length() + 1
    jump = []

    base = []
    for extra in range(max_budget + 1):
        cur = array('i', [0]) * n
        i = 0
        while i < n:
            reach = i if arr[i] == 0 else i + arr[i] + extra
            cur[i] = n - 1 if reach >= n else reach
            i += 1
        base.append(cur)
    jump.append(base)

    depth = 1
    while depth < levels_count:
        table = sparse_layers(jump[-1], n)
        source = jump[-1]
        produced = []
        cost = 0
        while cost <= max_budget:
            cur = array('i', [0]) * n
            i = 0
            while i < n:
                best = i
                first = 0
                while first <= cost:
                    mid = source[first][i]
                    val = rmq(table, logs, cost - first, i, mid)
                    if val > best:
                        best = val
                    first += 1
                cur[i] = best
                i += 1
            produced.append(cur)
            cost += 1
        jump.append(produced)
        depth += 1

    answers = [0] * q
    states = []
    active = []
    for query in packed:
        l, r, k, idx = query
        if l != r:
            active.append(len(states))
            states.append([[l] * (k + 1), 0, l, r, k, idx])

    bit = levels_count - 1
    while bit >= 0:
        if not active:
            break
        table = sparse_layers(jump[bit], n)
        for sid in active:
            far, hops, l, r, k, idx = states[sid]
            updated = [l] * (k + 1)
            cost = 0
            while cost <= k:
                best = l
                used = 0
                while used <= cost:
                    right = far[used]
                    if right >= n:
                        right = n - 1
                    val = rmq(table, logs, cost - used, l, right)
                    if val > best:
                        best = val
                    used += 1
                updated[cost] = best
                cost += 1
            if updated[k] < r:
                states[sid] = [updated, hops + (1 << bit), l, r, k, idx]
        bit -= 1

    for far, hops, l, r, k, idx in states:
        answers[idx] = -1 if far[k] < r else hops + 1

    sys.stdout.write("\n".join(str(x) for x in answers))

# CLAUSE: finish_program
main()
