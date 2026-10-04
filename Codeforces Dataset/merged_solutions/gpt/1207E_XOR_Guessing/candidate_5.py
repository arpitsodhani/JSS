# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        q1 = list(range(1, 101))
        print("?", *q1, flush=True)
        r1 = int(sys.stdin.readline())

        q2 = [i << 7 for i in range(1, 101)]
        print("?", *q2, flush=True)
        r2 = int(sys.stdin.readline())

        ans = (r1 & (~127)) | (r2 & 127)
        print("!", ans, flush=True)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
