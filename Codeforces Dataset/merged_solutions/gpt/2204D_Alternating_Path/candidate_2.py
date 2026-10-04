# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        g = [[] for _ in range(n)]
        for _ in range(m):
            u = data[idx] - 1
            v = data[idx + 1] - 1
            idx += 2
            g[u].append(v)
            g[v].append(u)
        color = [-1] * n
        total = 0
        for s in range(n):
            if color[s] != -1:
                continue
            q = deque([s])
            color[s] = 0
            cnt = [1, 0]
            ok = True
            while q:
                v = q.popleft()
                for to in g[v]:
                    if color[to] == -1:
                        color[to] = color[v] ^ 1
                        cnt[color[to]] += 1
                        q.append(to)
                    elif color[to] == color[v]:
                        ok = False
            if ok:
                total += max(cnt)
        ans.append(str(total))
    sys.stdout.write('\n'.join(ans))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
