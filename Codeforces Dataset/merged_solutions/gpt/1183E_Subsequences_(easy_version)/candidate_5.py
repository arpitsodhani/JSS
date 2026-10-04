# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = sys.stdin.read().split()
            n = int(data[0])
            k = int(data[1])
            s = data[2]

            cap = k
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            dp[0][0] = 1
            last = [-1] * 26

            for i, ch in enumerate(s, 1):
                c = ord(ch) - 97
                for l in range(n + 1):
                    dp[i][l] = dp[i - 1][l]
                for l in range(1, i + 1):
                    dp[i][l] += dp[i - 1][l - 1]
                    if last[c] != -1:
                        dp[i][l] -= dp[last[c]][l - 1]
                    if dp[i][l] > cap:
                        dp[i][l] = cap
                last[c] = i - 1

            ans = 0
            need = k
            for l in range(n, -1, -1):
                take = min(need, dp[n][l])
                ans += take * (n - l)
                need -= take
                if need == 0:
                    print(ans)
                    return

            print(-1)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
