# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        out = []
        idx = 1

        for _ in range(t):
            s = data[idx] + data[idx + 1] + data[idx + 2]
            idx += 3
            out.append("0" if s % 3 == 0 else "1")

        print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
