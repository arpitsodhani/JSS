# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 10**9 + 7

        def main():
            input = sys.stdin.readline
            n, m = map(int, input().split())
            s = [input().strip() for _ in range(n)]

            right = [[m] * m for _ in range(n)]
            down = [[n] * m for _ in range(n)]

            for i in range(n):
                last = m
                for j in range(m - 1, -1, -1):
                    if s[i][j] == 'R':
                        last = j
                    right[i][j] = last

            for j in range(m):
                last = n
                for i in range(n - 1, -1, -1):
                    if s[i][j] == 'R':
                        last = i
                    down[i][j] = last

            dp = [[0] * m for _ in range(n)]
            pref_row = [[0] * (m + 1) for _ in range(n)]
            pref_col = [[0] * m for _ in range(n + 1)]

            dp[0][0] = 1
            pref_row[0][1] = 1
            pref_col[1][0] = 1

            for i in range(n):
                for j in range(m):
                    if i == 0 and j == 0:
                        continue

                    val = 0

                    if j > 0:
                        l = max(0, right[i][j] - (m - j))
                        val += pref_row[i][j] - pref_row[i][l]

                    if i > 0:
                        u = max(0, down[i][j] - (n - i))
                        val += pref_col[i][j] - pref_col[u][j]

                    dp[i][j] = val % MOD

                    pref_row[i][j + 1] = (pref_row[i][j] + dp[i][j]) % MOD
                    pref_col[i + 1][j] = (pref_col[i][j] + dp[i][j]) % MOD

                if i + 1 < n:
                    for j in range(m):
                        if pref_col[i + 1][j] == 0:
                            pref_col[i + 1][j] = pref_col[i][j]

            print(dp[n - 1][m - 1] % MOD)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
