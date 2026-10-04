import sys
from collections import deque

def flip_bits(a, l, r):
    for i in range(l, r + 1):
        a[i] ^= 1

def solve_case(n, s, t):
    start = int(s, 2)
    target = int(t, 2)

    if start == target:
        return []

    total = 1 << n
    parent = [-1] * total
    move = [None] * total
    parent[start] = start
    q = deque([start])

    masks = []
    for l in range(n):
        m = 0
        for r in range(l, n):
            m |= 1 << (n - 1 - r)
            if r > l:
                masks.append((l, r, m))

    while q:
        x = q.popleft()
        bits = [(x >> (n - 1 - i)) & 1 for i in range(n)]

        for l, r, m in masks:
            ok = True
            i, j = l, r
            while i < j:
                if bits[i] != bits[j]:
                    ok = False
                    break
                i += 1
                j -= 1
            if not ok:
                continue

            y = x ^ m
            if parent[y] == -1:
                parent[y] = x
                move[y] = (l + 1, r + 1)
                if y == target:
                    q.clear()
                    break
                q.append(y)

    if parent[target] == -1:
        return []

    ans = []
    cur = target
    while cur != start:
        ans.append(move[cur])
        cur = parent[cur]
    ans.reverse()
    return ans

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    tc = int(next(it))
    out = []

    for _ in range(tc):
        n = int(next(it))
        s = next(it).strip()
        t = next(it).strip()
        ans = solve_case(n, s, t)
        out.append(str(len(ans)))
        for l, r in ans:
            out.append(f"{l} {r}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
