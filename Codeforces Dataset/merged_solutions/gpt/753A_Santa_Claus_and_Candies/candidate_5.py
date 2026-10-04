# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        n = int(sys.stdin.readline())

        ans = []
        cur = 1
        while n >= cur:
            ans.append(cur)
            n -= cur
            cur += 1

        if n:
            ans[-1] += n

        print(len(ans))
        print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
