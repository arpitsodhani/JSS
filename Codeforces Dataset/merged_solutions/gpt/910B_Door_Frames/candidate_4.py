# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().split()
    if len(data) == 3:
        n, a, b = map(int, data)
    else:
        s = data[0]
        n, a, b = map(int, s)

    patterns = []
    for x in range(5):
        for y in range(3):
            if x == 0 and y == 0:
                continue
            if x * a + y * b <= n:
                patterns.append((x, y))

    inf = 10**9
    dp = [[inf] * 3 for _ in range(5)]
    dp[0][0] = 0

    for i in range(5):
        for j in range(3):
            if dp[i][j] == inf:
                continue
            for x, y in patterns:
                ni = min(4, i + x)
                nj = min(2, j + y)
                dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1)

    print(dp[4][2])

# CLAUSE: finish_program
def main():
    _inner_main()

main()
