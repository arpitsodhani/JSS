import sys
from collections import deque

def can_escape(n, rows):
    sr = 0
    for i in range(3):
        if 's' in rows[i]:
            sr = i
            break

    def blocked(r, c, t, shift):
        idx = c + 2 * t + shift
        return idx < n and rows[r][idx] not in '.s'

    q = deque([(sr, 0)])
    seen = [[False] * (n + 1) for _ in range(3)]
    seen[sr][0] = True

    while q:
        r, c = q.popleft()
        t = c

        if c >= n - 1:
            return True

        if blocked(r, c, t, 0):
            continue

        nc = c + 1
        for nr in (r - 1, r, r + 1):
            if 0 <= nr < 3:
                if nc >= n:
                    return True
                if all(not blocked(nr, nc, t, sh) for sh in (0, 1, 2)):
                    if not seen[nr][nc]:
                        seen[nr][nc] = True
                        q.append((nr, nc))

    return False

data = sys.stdin.read().split()
if data:
    t = int(data[0])
    p = 1
    ans = []
    for _ in range(t):
        n = int(data[p])
        p += 2
        rows = data[p:p + 3]
        p += 3
        ans.append("YES" if can_escape(n, rows) else "NO")
    print("\n".join(ans))
