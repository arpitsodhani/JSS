# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split()
        n = int(data[0])
        s = int(data[1]) - 1
        k = int(data[2])
        r = list(map(int, data[3:3 + n]))
        c = data[3 + n].strip()

        INF = 10 ** 18
        dp = [[INF] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][min(k, r[i])] = abs(s - i)

        order = sorted(range(n), key=lambda x: r[x])

        for i in order:
            for total in range(k + 1):
                cur = dp[i][total]
                if cur == INF:
                    continue
                for j in range(n):
                    if r[j] > r[i] and c[j] != c[i]:
                        ntotal = min(k, total + r[j])
                        ncost = cur + abs(i - j)
                        if ncost < dp[j][ntotal]:
                            dp[j][ntotal] = ncost

        ans = min(dp[i][k] for i in range(n))
        print(ans if ans < INF else -1)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
