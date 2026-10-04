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
            s = data[1]

            colors = "RGB"
            INF = 10**9

            dp = [[INF] * 3 for _ in range(n)]
            parent = [[-1] * 3 for _ in range(n)]

            for c in range(3):
                dp[0][c] = 0 if s[0] == colors[c] else 1

            for i in range(1, n):
                for c in range(3):
                    cost = 0 if s[i] == colors[c] else 1
                    for p in range(3):
                        if p != c and dp[i - 1][p] + cost < dp[i][c]:
                            dp[i][c] = dp[i - 1][p] + cost
                            parent[i][c] = p

            last = min(range(3), key=lambda c: dp[n - 1][c])
            ans = [""] * n

            cur = last
            for i in range(n - 1, -1, -1):
                ans[i] = colors[cur]
                cur = parent[i][cur]

            print(dp[n - 1][last])
            print("".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
