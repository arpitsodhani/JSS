# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        x = int(input())
        print(x.bit_count())

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
