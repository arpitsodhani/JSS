# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        if data:
            n = data[0]
            arr = data[1:1 + n]
            arr.sort()
            print(*arr)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
