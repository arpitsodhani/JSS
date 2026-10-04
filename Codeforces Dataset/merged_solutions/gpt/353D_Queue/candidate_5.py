# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        s = sys.stdin.readline().strip()

        boys = 0
        ans = 0

        for c in s:
            if c == 'M':
                boys += 1
            elif boys:
                ans = max(ans + 1, boys)

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
