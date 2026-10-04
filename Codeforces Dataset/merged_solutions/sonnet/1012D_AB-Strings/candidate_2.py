# CLAUSE: setup_environment
import sys
from collections import deque

def good(s, t):
    return (s.count('a') == len(s) and t.count('b') == len(t)) or (s.count('b') == len(s) and t.count('a') == len(t))

def compact(x):
    y = []
    for c in x:
        if not y or y[-1] != c:
            y.append(c)
    return ''.join(y)

def step(s, t, i, j):
    return t[:j] + s[i:], s[:i] + t[j:]

def restore(state, parent, used):
    ans = []
    while parent[state] is not None:
        ans.append(used[state])
        state = parent[state]
    ans.reverse()
    out = [str(len(ans))]
    out.extend(f"{i} {j}" for i, j in ans)
    sys.stdout.write("\n".join(out))

# CLAUSE: solve_logic
def solve():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    s, t = data[0], data[1]
    if good(s, t):
        print(0)
        return

    start = (s, t)
    total = len(s) + len(t)
    q = deque([start])
    parent = {start: None}
    used = {}

    while q:
        cs, ct = q.popleft()
        for i in range(len(cs) + 1):
            for j in range(len(ct) + 1):
                if i == 0 and j == 0:
                    continue
                ns, nt = step(cs, ct, i, j)
                nxt = (ns, nt)
                if nxt in parent:
                    continue
                parent[nxt] = (cs, ct)
                used[nxt] = (i, j)
                if good(ns, nt):
                    restore(nxt, parent, used)
                    return
                if compact(ns) == ns and compact(nt) == nt and len(ns) + len(nt) == total:
                    q.append(nxt)

    ac = s.count('a') + t.count('a')
    bc = total - ac
    targets = {('a' * ac, 'b' * bc), ('b' * bc, 'a' * ac)}
    q = deque([start])
    parent = {start: None}
    used = {}

    while q:
        cs, ct = q.popleft()
        for i in range(len(cs) + 1):
            for j in range(len(ct) + 1):
                if i == 0 and j == 0:
                    continue
                nxt = step(cs, ct, i, j)
                if nxt in parent:
                    continue
                parent[nxt] = (cs, ct)
                used[nxt] = (i, j)
                if nxt in targets:
                    restore(nxt, parent, used)
                    return
                q.append(nxt)

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
