# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        n, m, r = map(int, input().split())
        s = list(map(int, input().split()))
        b = list(map(int, input().split()))

        mn = min(s)
        mx = max(b)

        if mx <= mn:
            print(r)
        else:
            shares = r // mn
            print((r % mn) + shares * mx)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
