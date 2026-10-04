# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        t = int(input())
        for _ in range(t):
            x = list(map(int, input().split()))
            print(max(x) - min(x))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
