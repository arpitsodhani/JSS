# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        n, k = map(int, sys.stdin.readline().split())

        best = 1
        r = int(math.isqrt(n))

        for i in range(1, r + 1):
            if n % i == 0:
                if i < k and i > best:
                    best = i
                d = n // i
                if d < k and d > best:
                    best = d

        print((n // best) * k + best)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
