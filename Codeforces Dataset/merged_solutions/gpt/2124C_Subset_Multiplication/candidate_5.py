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
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            b = data[idx:idx + n]
            idx += n

            x = 1
            for i in range(n - 1):
                if b[i + 1] % b[i] != 0:
                    x = x * (b[i] // gcd(b[i], b[i + 1])) // gcd(x, b[i] // gcd(b[i], b[i + 1]))

            ans.append(str(x))

        sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
