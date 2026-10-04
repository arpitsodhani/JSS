# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    a = data[1:1 + n]

    mx = max(a)
    cnt = [0] * (mx + 1)

    for x in a:
        cnt[x] += 1

    dp = [0] * (mx + 1)
    ans = 0

    for x in range(mx, 0, -1):
        if cnt[x]:
            best = 0
            for y in range(x + x, mx + 1, x):
                if dp[y] > best:
                    best = dp[y]
            dp[x] = cnt[x] + best
            if dp[x] > ans:
                ans = dp[x]

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
