# CLAUSE: setup_environment
import sys
from array import array

def make_logs(n):
    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1
    return logs

def sparse_by_cost(rows, n):
    built = []
    for row in rows:
        levels = [row]
        step = 1
        while step + step <= n:
            prev = levels[-1]
            size = n - step - step + 1
            cur = array('i', [0]) * size
            for i in range(size):
                x = prev[i]
                y = prev[i + step]
                cur[i] = x if x >= y else y
            levels.append(cur)
            step += step
        built.append(levels)
    return built

def get_max(st, logs, cost, left, right):
    if right < left:
        return left
    length = right - left + 1
    p = logs[length]
    layer = st[cost][p]
    x = layer[left]
    y = layer[right - (1 << p) + 1]
    return x if x >= y else y

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    at = 0
    n = data[at]
    q = data[at + 1]
    at += 2
    a = data[at:at + n]
    at += n

    queries = []
    max_k = 0
    for qi in range(q):
        l = data[at] - 1
        r = data[at + 1] - 1
        k = data[at + 2]
        at += 3
        queries.append((l, r, k, qi))
        if k > max_k:
            max_k = k

    logs = make_logs(n)
    height = (n + 1).bit_length() + 1

    jumps = []
    first = []
    for c in range(max_k + 1):
        row = array('i', [0]) * n
        for i, x in enumerate(a):
            if x == 0:
                row[i] = i
            else:
                z = i + x + c
                row[i] = n - 1 if z >= n else z
        first.append(row)
    jumps.append(first)

    for _ in range(height - 1):
        st = sparse_by_cost(jumps[-1], n)
        block = []
        old = jumps[-1]
        for c in range(max_k + 1):
            row = array('i', [0]) * n
            for i in range(n):
                best = i
                for spend in range(c + 1):
                    mid = old[spend][i]
                    got = get_max(st, logs, c - spend, i, mid)
                    if got > best:
                        best = got
                row[i] = best
            block.append(row)
        jumps.append(block)

    ans = [0] * q
    states = []
    active = []
    for l, r, k, qi in queries:
        if l == r:
            ans[qi] = 0
        else:
            active.append(len(states))
            states.append(([l] * (k + 1), 0, l, r, k, qi))

    for level in range(height - 1, -1, -1):
        if not active:
            break
        st = sparse_by_cost(jumps[level], n)
        for sid in active:
            far, hops, l, r, k, qi = states[sid]
            nf = [l] * (k + 1)
            for cost in range(k + 1):
                best = l
                for used in range(cost + 1):
                    right = far[used]
                    if right >= n:
                        right = n - 1
                    got = get_max(st, logs, cost - used, l, right)
                    if got > best:
                        best = got
                nf[cost] = best
            if nf[k] < r:
                states[sid] = (nf, hops + (1 << level), l, r, k, qi)

    for far, hops, l, r, k, qi in states:
        ans[qi] = -1 if far[k] < r else hops + 1

    sys.stdout.write("\n".join(map(str, ans)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
