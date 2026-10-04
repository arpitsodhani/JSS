# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        n = int(sys.stdin.readline())

        if n % 2:
            print("black")
        else:
            print("white")
            print("1 2")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
