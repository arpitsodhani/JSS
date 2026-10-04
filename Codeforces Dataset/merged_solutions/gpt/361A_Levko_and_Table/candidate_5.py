# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split()
        n = int(data[0])
        k = int(data[1])

        for i in range(n):
            row = ["0"] * n
            row[i] = str(k)
            print(" ".join(row))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
