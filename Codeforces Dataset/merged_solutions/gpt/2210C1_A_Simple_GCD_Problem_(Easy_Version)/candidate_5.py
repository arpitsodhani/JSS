# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from math import gcd

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        ans = []

        for _ in range(t):
            n = data[p]
            p += 1
            a = data[p:p + n]
            p += n
            p += n

            if n == 2:
                g = gcd(a[0], a[1])
                ans.append(str((g < a[0]) + (g < a[1])))
                continue

            res = 0
            g = [gcd(a[i], a[i + 1]) for i in range(n - 1)]

            if g[0] < a[0]:
                res += 1
            if g[-1] < a[-1]:
                res += 1

            for i in range(1, n - 1):
                x = g[i - 1]
                y = g[i]
                l = x // gcd(x, y) * y
                if l < a[i]:
                    res += 1

            ans.append(str(res))

        sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
