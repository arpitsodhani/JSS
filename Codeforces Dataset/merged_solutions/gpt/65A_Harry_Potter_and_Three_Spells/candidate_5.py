# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        a, b, c, d, e, f = map(int, sys.stdin.read().split())

        if b * d * f > a * c * e:
            print("Ron")
        else:
            print("Hermione")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
