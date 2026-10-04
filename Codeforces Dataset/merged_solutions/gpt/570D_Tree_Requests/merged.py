# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    parents = list(map(int, input().split()))
    s = input().strip()

    children = [[] for _ in range(n)]
    for i, p in enumerate(parents, start=1):
        children[p - 1].append(i)

    tin = [0] * n
    tout = [0] * n
    depth = [0] * n
    by_depth = {}
    timer = 0

    stack = [(0, 1, 0)]
    while stack:
        v, d, state = stack.pop()
        if state == 0:
            tin[v] = timer
            timer += 1
            depth[v] = d
            if d not in by_depth:
                by_depth[d] = [[], [0]]
            arr, pref = by_depth[d]
            arr.append(tin[v])
            pref.append(pref[-1] ^ (1 << (s[v] - 97)))
            stack.append((v, d, 1))
            for u in reversed(children[v]):
                stack.append((u, d + 1, 0))
        else:
            tout[v] = timer

    ans = []
    for _ in range(m):
        v, h = map(int, input().split())
        v -= 1
        data = by_depth.get(h)
        if data is None:
            ans.append("Yes")
            continue
        arr, pref = data
        l = bisect_left(arr, tin[v])
        r = bisect_left(arr, tout[v])
        mask = pref[r] ^ pref[l]
        ans.append("Yes" if mask & (mask - 1) == 0 else "No")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
