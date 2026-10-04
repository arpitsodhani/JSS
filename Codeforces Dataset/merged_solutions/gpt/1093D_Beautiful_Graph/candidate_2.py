# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    max_n = 300000
    pow2 = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD
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
        ans = 1
        ok = True
        for s in range(n):
            if color[s] != -1:
                continue
            q = deque([s])
            color[s] = 0
            cnt = [1, 0]
            while q and ok:
                u = q.popleft()
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        cnt[color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
            if not ok:
                break
            ans = ans * (pow2[cnt[0]] + pow2[cnt[1]]) % MOD
        out.append(str(ans if ok else 0))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
