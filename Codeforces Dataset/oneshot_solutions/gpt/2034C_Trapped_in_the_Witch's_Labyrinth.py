import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    p = 1
    out = []
    dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    rev_dirs = [(-1, 0, 'D'), (1, 0, 'U'), (0, -1, 'R'), (0, 1, 'L')]

    for _ in range(t):
        n = int(data[p])
        m = int(data[p + 1])
        p += 2
        g = data[p:p + n]
        p += n

        safe = [[False] * m for _ in range(n)]
        rem = [[0] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                c = g[i][j]
                if c == '?':
                    cnt = 0
                    for di, dj in dirs.values():
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            cnt += 1
                    rem[i][j] = cnt
                    if cnt == 0:
                        safe[i][j] = True
                        q.append((i, j))
                else:
                    di, dj = dirs[c]
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < n and 0 <= nj < m):
                        safe[i][j] = True
                        q.append((i, j))

        while q:
            i, j = q.popleft()
            for di, dj, need in rev_dirs:
                pi, pj = i + di, j + dj
                if not (0 <= pi < n and 0 <= pj < m) or safe[pi][pj]:
                    continue
                c = g[pi][pj]
                if c == need:
                    safe[pi][pj] = True
                    q.append((pi, pj))
                elif c == '?':
                    rem[pi][pj] -= 1
                    if rem[pi][pj] == 0:
                        safe[pi][pj] = True
                        q.append((pi, pj))

        ans = 0
        for i in range(n):
            for j in range(m):
                if not safe[i][j]:
                    ans += 1
        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
