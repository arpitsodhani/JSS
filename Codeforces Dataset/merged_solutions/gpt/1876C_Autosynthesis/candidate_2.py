# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = [0] + data[1:1 + n]
    children = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i] <= n:
            children[a[i]].append(i)
            indeg[a[i]] += 1
    q = deque((i for i in range(1, n + 1) if indeg[i] == 0))
    removed = [False] * (n + 1)
    order = []
    while q:
        v = q.popleft()
        if removed[v]:
            continue
        removed[v] = True
        order.append(v)
        if a[v] <= n:
            p = a[v]
            indeg[p] -= 1
            if indeg[p] == 0:
                q.append(p)
    on_cycle = [not removed[i] for i in range(n + 1)]
    A = [False] * (n + 1)
    B = [False] * (n + 1)
    C = [False] * (n + 1)
    for v in order:
        all_b = True
        all_ab = True
        any_a = False
        for ch in children[v]:
            if on_cycle[ch]:
                continue
            if not B[ch]:
                all_b = False
            if not (A[ch] or B[ch]):
                all_ab = False
            if A[ch]:
                any_a = True
        A[v] = a[v] <= n and all_b
        B[v] = all_ab and any_a
        C[v] = all_b
    state = [-1] * (n + 1)
    for v in range(1, n + 1):
        if a[v] > n:
            if not B[v]:
                print(-1)
                return
            state[v] = 0
    seen_cycle = [False] * (n + 1)
    for start in range(1, n + 1):
        if not on_cycle[start] or seen_cycle[start]:
            continue
        cyc = []
        v = start
        while not seen_cycle[v]:
            seen_cycle[v] = True
            cyc.append(v)
            v = a[v]
        m = len(cyc)
        ft = [False] * m
        sc = [False] * m
        sn = [False] * m
        for idx, node in enumerate(cyc):
            all_b = True
            all_ab = True
            any_a = False
            for ch in children[node]:
                if on_cycle[ch]:
                    continue
                if not B[ch]:
                    all_b = False
                if not (A[ch] or B[ch]):
                    all_ab = False
                if A[ch]:
                    any_a = True
            ft[idx] = all_b
            sn[idx] = all_b
            sc[idx] = all_ab and any_a

        def ok(prev, cur, idx):
            if cur == 1:
                return prev == 0 and ft[idx]
            return sc[idx] or (sn[idx] and prev == 1)
        colors = None
        for first in (0, 1):
            dp = [[False, False] for _ in range(m)]
            par = [[-1, -1] for _ in range(m)]
            dp[0][first] = True
            for i in range(1, m):
                for prev in (0, 1):
                    if not dp[i - 1][prev]:
                        continue
                    for cur in (0, 1):
                        if ok(prev, cur, i):
                            dp[i][cur] = True
                            par[i][cur] = prev
            for last in (0, 1):
                if dp[m - 1][last] and ok(last, first, 0):
                    colors = [0] * m
                    colors[m - 1] = last
                    for i in range(m - 1, 0, -1):
                        colors[i - 1] = par[i][colors[i]]
                    break
            if colors is not None:
                break
        if colors is None:
            print(-1)
            return
        for idx, node in enumerate(cyc):
            if colors[idx] == 1:
                state[node] = 1
            elif sc[idx]:
                state[node] = 0
            else:
                state[node] = 2
    stack = [i for i in range(1, n + 1) if state[i] != -1]
    while stack:
        v = stack.pop()
        st = state[v]
        childs = [ch for ch in children[v] if not on_cycle[ch]]
        if st == 1:
            for ch in childs:
                state[ch] = 0
                stack.append(ch)
        elif st == 2:
            for ch in childs:
                state[ch] = 0
                stack.append(ch)
        else:
            chosen = -1
            for ch in childs:
                if A[ch]:
                    chosen = ch
                    break
            if chosen == -1:
                print(-1)
                return
            for ch in childs:
                if ch == chosen:
                    state[ch] = 1
                elif B[ch]:
                    state[ch] = 0
                else:
                    state[ch] = 1
                stack.append(ch)
    ans = []
    for i in range(1, n + 1):
        if state[i] == 1:
            ans.append(a[i])
    print(len(ans))
    if ans:
        print(*ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
