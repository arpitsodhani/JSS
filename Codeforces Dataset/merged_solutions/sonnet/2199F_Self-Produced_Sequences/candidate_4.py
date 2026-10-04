# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def solve_one(a):
    dp = {0: 1}

    for x in a:
        items = list(dp.items())
        for s, ways in items:
            if x == 0:
                dp[s] = (dp[s] + ways) % MOD
            elif s == x:
                ns = s + x
                dp[ns] = (dp.get(ns, 0) + ways) % MOD
            elif s == 3 * x:
                dp[s] = (dp[s] + ways) % MOD

    answer = 0
    for ways in dp.values():
        answer += ways
    return answer % MOD

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    k = 0
    t = int(data[k])
    k += 1
    res = []

    for _ in range(t):
        n = int(data[k])
        k += 1
        current = []
        for _ in range(n):
            current.append(int(data[k]))
            k += 1
        res.append(str(solve_one(current)))

    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
