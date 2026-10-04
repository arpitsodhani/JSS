# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 1000000009

        n, w, b = map(int, sys.stdin.readline().split())

        if n < 3 or w < 2 or b < 1:
            print(0)
            sys.exit()

        m = max(w, b)
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def c(a, k):
            if k < 0 or k > a:
                return 0
            return fact[a] * invfact[k] % MOD * invfact[a - k] % MOD

        ans = 0
        lo = max(1, n - w)
        hi = min(b, n - 2)

        for y in range(lo, hi + 1):
            ans = (ans + (n - y - 1) * c(w - 1, n - y - 1) * c(b - 1, y - 1)) % MOD

        ans = ans * fact[w] % MOD * fact[b] % MOD
        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
