# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().split()
        if not data:
            return

        n = int(data[0])
        m = int(data[1])
        g = [[] for _ in range(n)]

        p = 2
        for _ in range(m):
            a = int(data[p]) - 1
            b = int(data[p + 1]) - 1
            c = ord(data[p + 2]) - 97
            p += 3
            g[a].append((b, c))

        dp = [[[-1] * 26 for _ in range(n)] for _ in range(n)]
        sys.setrecursionlimit(1000000)

        def win(v, u, last):
            if dp[v][u][last] != -1:
                return dp[v][u][last]

            dp[v][u][last] = 0
            for to, ch in g[v]:
                if ch >= last and not win(u, to, ch):
                    dp[v][u][last] = 1
                    break

            return dp[v][u][last]

        ans = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('A' if win(i, j, 0) else 'B')
            ans.append(''.join(row))

        print('\n'.join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
