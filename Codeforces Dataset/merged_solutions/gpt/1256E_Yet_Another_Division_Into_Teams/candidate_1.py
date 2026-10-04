# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]

    students = sorted((a[i], i) for i in range(n))
    vals = [0] + [x for x, _ in students]

    inf = 10 ** 30
    dp = [inf] * (n + 1)
    parent = [-1] * (n + 1)
    dp[0] = 0

    best_val = inf
    best_j = -1

    for i in range(3, n + 1):
        j = i - 3
        cur = dp[j] - vals[j + 1]
        if cur < best_val:
            best_val = cur
            best_j = j
        dp[i] = vals[i] + best_val
        parent[i] = best_j

    ans = [0] * n
    teams = 0
    i = n
    while i > 0:
        teams += 1
        j = parent[i]
        for p in range(j + 1, i + 1):
            ans[students[p - 1][1]] = teams
        i = j

    print(dp[n], teams)
    print(*ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
