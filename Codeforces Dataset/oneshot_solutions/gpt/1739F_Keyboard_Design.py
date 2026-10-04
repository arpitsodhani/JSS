import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    nxt = [[-1] * 12]
    link = [0]
    cost = [0]

    def add_node():
        nxt.append([-1] * 12)
        link.append(0)
        cost.append(0)
        return len(nxt) - 1

    def add_string(s, w):
        v = 0
        for ch in s:
            x = ord(ch) - 97
            if nxt[v][x] == -1:
                nxt[v][x] = add_node()
            v = nxt[v][x]
        cost[v] += w

    ptr = 1
    for _ in range(n):
        w = int(data[ptr])
        s = data[ptr + 1]
        ptr += 2

        adj = [set() for _ in range(12)]
        used = set()
        for i in range(len(s) - 1):
            a = ord(s[i]) - 97
            b = ord(s[i + 1]) - 97
            adj[a].add(b)
            adj[b].add(a)
            used.add(a)
            used.add(b)

        bad = False
        start = -1
        for x in used:
            if len(adj[x]) > 2:
                bad = True
                break
            if len(adj[x]) == 1:
                start = x

        if bad or start == -1:
            continue

        res = []
        prev = -1
        cur = start
        while True:
            res.append(cur)
            go = -1
            for y in adj[cur]:
                if y != prev:
                    go = y
                    break
            if go == -1:
                break
            prev, cur = cur, go

        if len(res) != len(used):
            continue

        pos = [-1] * 12
        for i, x in enumerate(res):
            pos[x] = i

        for i in range(len(s) - 1):
            a = ord(s[i]) - 97
            b = ord(s[i + 1]) - 97
            if abs(pos[a] - pos[b]) != 1:
                bad = True
                break

        if bad:
            continue

        t = ''.join(chr(97 + x) for x in res)
        add_string(t, w)
        add_string(t[::-1], w)

    q = deque()
    for c in range(12):
        u = nxt[0][c]
        if u == -1:
            nxt[0][c] = 0
        else:
            q.append(u)

    while q:
        v = q.popleft()
        cost[v] += cost[link[v]]
        for c in range(12):
            u = nxt[v][c]
            if u == -1:
                nxt[v][c] = nxt[link[v]][c]
            else:
                link[u] = nxt[link[v]][c]
                q.append(u)

    full = (1 << 12) - 1
    dp = [dict() for _ in range(1 << 12)]
    dp[0][0] = 0

    for mask in range(1 << 12):
        if not dp[mask]:
            continue
        bits0 = full ^ mask
        for state, val in list(dp[mask].items()):
            bits = bits0
            while bits:
                lb = bits & -bits
                c = lb.bit_length() - 1
                ns = nxt[state][c]
                nm = mask | lb
                nv = val + cost[ns]
                old = dp[nm].get(ns)
                if old is None or nv > old:
                    dp[nm][ns] = nv
                bits -= lb

    state = max(dp[full], key=lambda x: dp[full][x])
    mask = full
    ans = []

    while mask:
        cur_val = dp[mask][state]
        bits = mask
        done = False
        while bits and not done:
            lb = bits & -bits
            c = lb.bit_length() - 1
            pm = mask ^ lb
            for ps, pv in dp[pm].items():
                if nxt[ps][c] == state and pv + cost[state] == cur_val:
                    ans.append(chr(97 + c))
                    mask = pm
                    state = ps
                    done = True
                    break
            bits -= lb

    print(''.join(ans))

if __name__ == "__main__":
    main()
