# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n

        suf = [0] * n
        suf[-1] = a[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(a[i], suf[i + 1])

        moved = []
        ans = []
        add_min = 10 ** 18

        for i, x in enumerate(a):
            if moved:
                add_min = moved[0]
            else:
                add_min = 10 ** 18

            if i + 1 < n and x > suf[i + 1]:
                heappush(moved, x + 1)
            else:
                while moved and moved[0] <= x:
                    ans.append(heappop(moved))
                ans.append(x)

        while moved:
            ans.append(heappop(moved))

        out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
