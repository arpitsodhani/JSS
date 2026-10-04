# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = sys.stdin.read().strip().split()
        if not data:
            return

        t = int(data[0])
        idx = 1
        out = []

        for _ in range(t):
            n = int(data[idx])
            s = data[idx + 1]
            idx += 2

            twos = [i for i, c in enumerate(s) if c == '2']

            if len(twos) in (1, 2):
                out.append("NO")
                continue

            ans = [['=' for _ in range(n)] for _ in range(n)]
            for i in range(n):
                ans[i][i] = 'X'

            m = len(twos)
            for i in range(m):
                a = twos[i]
                b = twos[(i + 1) % m]
                ans[a][b] = '+'
                ans[b][a] = '-'

            out.append("YES")
            out.extend(''.join(row) for row in ans)

        sys.stdout.write('\n'.join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
