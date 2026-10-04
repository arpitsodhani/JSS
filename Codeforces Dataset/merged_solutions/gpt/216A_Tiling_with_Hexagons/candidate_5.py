# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        a, b, c = map(int, sys.stdin.read().split())
        print(a * b + b * c + c * a - a - b - c + 1)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
