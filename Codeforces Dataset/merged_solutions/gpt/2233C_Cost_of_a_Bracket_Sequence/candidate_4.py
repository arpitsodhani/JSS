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
            k = int(data[idx + 1])
            s = data[idx + 2]
            idx += 3

            pref_open = [0] * (n + 1)
            for i, ch in enumerate(s):
                pref_open[i + 1] = pref_open[i] + (ch == '(')

            suff_close = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                suff_close[i] = suff_close[i + 1] + (s[i] == ')')

            best = n + 1
            cut = 0
            for i in range(n + 1):
                cur = pref_open[i] + suff_close[i]
                if cur < best:
                    best = cur
                    cut = i

            ans = ['0'] * n
            need = min(k, best)

            for i in range(cut):
                if need and s[i] == '(':
                    ans[i] = '1'
                    need -= 1

            for i in range(cut, n):
                if need and s[i] == ')':
                    ans[i] = '1'
                    need -= 1

            out.append(''.join(ans))

        sys.stdout.write('\n'.join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
