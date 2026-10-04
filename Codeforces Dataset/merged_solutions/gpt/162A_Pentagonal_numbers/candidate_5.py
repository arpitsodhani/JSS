# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        n = int(input())
        print((3 * n * n - n) // 2)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
