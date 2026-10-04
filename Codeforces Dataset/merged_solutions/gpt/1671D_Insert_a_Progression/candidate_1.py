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
        x = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        ans = 0
        mn = min(a)
        mx = max(a)

        for i in range(n - 1):
            ans += abs(a[i] - a[i + 1])

        if mn > 1:
            ans += min(a[0] - 1, a[-1] - 1, 2 * (mn - 1))

        if mx < x:
            ans += min(x - a[0], x - a[-1], 2 * (x - mx))

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
