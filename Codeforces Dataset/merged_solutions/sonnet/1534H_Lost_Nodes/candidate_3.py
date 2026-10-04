# CLAUSE: setup_environment
import sys

LOW = -10 ** 20

# CLAUSE: solve_logic
def packed_score(pairs):
    if not pairs:
        return 0
    nums = []
    for first, second in pairs:
        nums.append(first)
    nums.sort(reverse=True)
    best = len(nums)
    for at in range(len(nums)):
        val = nums[at] + at
        if val > best:
            best = val
    answer = best
    for removed, pair in enumerate(pairs):
        rest = []
        for idx, item in enumerate(pairs):
            if idx != removed:
                rest.append(item[0])
        rest.sort(reverse=True)
        now = len(rest)
        for at, val in enumerate(rest):
            now = max(now, val + at)
        now = max(now, pair[1])
        answer = min(answer, now)
    return answer

def make_transition(pairs):
    d = len(pairs)
    if d < 2:
        return [0] * d
    perm = list(range(d))
    perm.sort(key=lambda x: (-pairs[x][0], x))
    where = [0] * d
    costs = []
    bonus = []
    for i, original in enumerate(perm):
        where[original] = i
        costs.append(pairs[original][0])
        bonus.append(pairs[original][1])
    z0 = [costs[i] + i for i in range(d)]
    z1 = [costs[i] + i - 1 for i in range(d)]
    z2 = [costs[i] + i - 2 for i in range(d)]
    left0 = z0[:]
    right1 = z1[:]
    right2 = z2[:]
    for i in range(1, d):
        left0[i] = max(left0[i], left0[i - 1])
    for i in range(d - 2, -1, -1):
        right1[i] = max(right1[i], right1[i + 1])
        right2[i] = max(right2[i], right2[i + 1])
    def after_drop(x):
        ret = d - 1
        if x > 0:
            ret = max(ret, left0[x - 1])
        if x + 1 < d:
            ret = max(ret, right1[x + 1])
        return ret
    def after_pair(x, y):
        if x > y:
            x, y = y, x
        ret = d - 2
        if x > 0:
            ret = max(ret, left0[x - 1])
        middle = LOW
        for i in range(x + 1, y):
            if z1[i] > middle:
                middle = z1[i]
        ret = max(ret, middle)
        if y + 1 < d:
            ret = max(ret, right2[y + 1])
        return ret
    raw = [0] * d
    for removed in range(d):
        res = after_drop(removed)
        for chosen in range(d):
            if chosen != removed:
                alt = after_pair(removed, chosen)
                if bonus[chosen] > alt:
                    alt = bonus[chosen]
                if alt < res:
                    res = alt
        raw[removed] = res
    ans = [0] * d
    for original in range(d):
        ans[original] = raw[where[original]]
    return ans

def solve():
    inp = list(map(int, sys.stdin.buffer.read().split()))
    if not inp:
        return
    n = inp[0]
    graph = [[] for _ in range(n)]
    pos = 1
    while pos < len(inp):
        a = inp[pos] - 1
        b = inp[pos + 1] - 1
        pos += 2
        graph[a].append(b)
        graph[b].append(a)
    if n == 1:
        sys.stdout.write("0\n")
        return
    par = [-1] * n
    seq = [0]
    head = 0
    while head < len(seq):
        node = seq[head]
        head += 1
        for to in graph[node]:
            if to != par[node]:
                par[to] = node
                seq.append(to)
    c = {}
    d = {}
    for node in reversed(seq[1:]):
        cur = []
        for to in graph[node]:
            if to != par[node]:
                cur.append((c[(to, node)], d[(to, node)]))
        got = packed_score(cur)
        d[(node, par[node])] = got
        c[(node, par[node])] = got + 1
    for node in seq:
        incoming = []
        for to in graph[node]:
            if (to, node) not in c:
                break
            incoming.append((c[(to, node)], d[(to, node)]))
        else:
            vals = make_transition(incoming)
            for i, to in enumerate(graph[node]):
                d[(node, to)] = vals[i]
                c[(node, to)] = vals[i] + 1
    answer = 0
    for node in range(n):
        vals = []
        for to in graph[node]:
            vals.append(c[(to, node)])
        vals.sort(reverse=True)
        cur = len(vals)
        if vals:
            cur = max(cur, len(vals) - 1 + vals[0])
        top = vals[0] if vals else 0
        for i in range(1, len(vals)):
            cur = max(cur, top + vals[i] + i - 1)
        answer = max(answer, cur)
    sys.stdout.write(str(answer) + "\n")

# CLAUSE: finish_program
solve()
