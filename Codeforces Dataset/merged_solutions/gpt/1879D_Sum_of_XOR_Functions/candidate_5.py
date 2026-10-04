# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 998244353

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return
            n = data[0]
            a = data[1:1 + n]

            max_bits = max(a).bit_length() if a else 1
            ans = 0

            for bit in range(max_bits):
                cnt = [1, 0]
                sidx = [0, 0]
                parity = 0
                total = 0

                for j, x in enumerate(a, 1):
                    parity ^= (x >> bit) & 1
                    opp = parity ^ 1
                    total = (total + cnt[opp] * j - sidx[opp]) % MOD
                    cnt[parity] += 1
                    sidx[parity] += j

                ans = (ans + total * ((1 << bit) % MOD)) % MOD

            print(ans % MOD)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
