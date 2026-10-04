# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    trucks = []
    groups = {}
    p = 1
    for i in range(n):
        v, c, l, r = (data[p], data[p + 1], data[p + 2], data[p + 3])
        p += 4
        t = (v, c, l, l + c + r)
        trucks.append(t)
        groups.setdefault(l + c + r, []).append(i)
    prev = [-1] * n
    best_value = 0
    best_last = -1
    for total, ids in groups.items():
        dp = {0: 0}
        last = {0: -1}
        for idx in ids:
            v, c, l, _ = trucks[idx]
            cur = dp.get(l)
            if cur is None:
                continue
            nl = l + c
            nv = cur + v
            if nv > dp.get(nl, -1):
                dp[nl] = nv
                prev[idx] = last[l]
                last[nl] = idx
        val = dp.get(total)
        if val is not None and val > best_value:
            best_value = val
            best_last = last[total]
    ans = []
    while best_last != -1:
        ans.append(best_last + 1)
        best_last = prev[best_last]
    ans.reverse()
    print(len(ans))
    print(*ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
