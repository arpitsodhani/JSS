# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 10 ** 9 + 7
    MAX_N = 40000

    def is_pal(x):
        s = str(x)
        return s == s[::-1]

    pals = [i for i in range(1, MAX_N + 1) if is_pal(i)]

    dp = [0] * (MAX_N + 1)
    dp[0] = 1

    for p in pals:
        for s in range(p, MAX_N + 1):
            dp[s] = (dp[s] + dp[s - p]) % MOD

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []
    for i in range(1, t + 1):
        ans.append(str(dp[data[i]]))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
