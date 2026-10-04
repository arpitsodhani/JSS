# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        n = int(input())
        ans = 0
        v = 1
        while v <= n:
            v <<= 1
            ans += 1
        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
