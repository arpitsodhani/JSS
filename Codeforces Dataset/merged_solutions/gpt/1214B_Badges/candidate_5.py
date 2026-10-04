# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        b = int(input())
        g = int(input())
        n = int(input())

        lo = max(0, n - g)
        hi = min(b, n)

        print(max(0, hi - lo + 1))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
