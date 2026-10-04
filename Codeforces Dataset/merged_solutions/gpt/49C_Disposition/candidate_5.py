# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        n = int(sys.stdin.readline())
        ans = list(range(2, n + 1)) + [1]
        print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
