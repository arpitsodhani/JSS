# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 10**9 + 7
        INV2 = 500000004

        data = sys.stdin.read().split()
        t = int(data[0])
        out = []
        p = 1

        for _ in range(t):
            n = int(data[p])
            s = data[p + 1]
            p += 2

            carry = 0
            for ch in reversed(s[1:]):
                carry = (carry + (ch == '1')) * INV2 % MOD

            out.append(str((n - 1 + carry) % MOD))

        sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
