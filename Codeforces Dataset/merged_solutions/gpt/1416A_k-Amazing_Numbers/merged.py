# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        last = [0] * (n + 1)
        gap = [0] * (n + 1)

        for i, x in enumerate(a, 1):
            d = i - last[x]
            if d > gap[x]:
                gap[x] = d
            last[x] = i

        inf = n + 1
        ans = [inf] * (n + 2)

        for x in range(1, n + 1):
            if last[x]:
                d = n + 1 - last[x]
                if d > gap[x]:
                    gap[x] = d
                if x < ans[gap[x]]:
                    ans[gap[x]] = x

        best = inf
        res = []
        for k in range(1, n + 1):
            if ans[k] < best:
                best = ans[k]
            res.append(str(best if best != inf else -1))

        out.append(" ".join(res))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
