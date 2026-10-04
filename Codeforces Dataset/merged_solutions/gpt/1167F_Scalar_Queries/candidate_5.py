# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 10**9 + 7

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, v):
                n = self.n
                bit = self.bit
                while i <= n:
                    bit[i] = (bit[i] + v) % MOD
                    i += i & -i

            def sum(self, i):
                s = 0
                bit = self.bit
                while i > 0:
                    s = (s + bit[i]) % MOD
                    i -= i & -i
                return s

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return
            n = data[0]
            a = data[1:]

            items = sorted((v, i + 1) for i, v in enumerate(a))

            left_pos = Fenwick(n)
            right_weight = Fenwick(n)

            ans = 0
            total_right = 0

            for v, p in items:
                v %= MOD

                base = p * (n - p + 1) % MOD
                left_sum = left_pos.sum(p - 1)
                right_sum = (total_right - right_weight.sum(p)) % MOD

                extra = ((n - p + 1) * left_sum + p * right_sum) % MOD
                ans = (ans + v * (base + extra)) % MOD

                left_pos.add(p, p)
                w = n - p + 1
                right_weight.add(p, w)
                total_right = (total_right + w) % MOD

            print(ans % MOD)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
