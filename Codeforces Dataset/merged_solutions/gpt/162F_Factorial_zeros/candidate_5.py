# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        s = sys.stdin.read().strip()
        if s:
            n = int(s)
            ans = 0
            while n:
                n //= 5
                ans += n
            print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
