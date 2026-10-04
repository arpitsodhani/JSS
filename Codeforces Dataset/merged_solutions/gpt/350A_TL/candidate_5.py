# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n, m = data[0], data[1]
        correct = data[2:2 + n]
        wrong = data[2 + n:2 + n + m]

        v = max(max(correct), 2 * min(correct))

        if v < min(wrong):
            print(v)
        else:
            print(-1)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
