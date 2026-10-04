# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().strip().split()
        if not data:
            sys.exit()

        q = int(data[0])
        ans = []

        for i in range(1, q + 1):
            t = data[i]
            if '0' not in t or '1' not in t:
                ans.append(t)
            else:
                ans.append('01' * len(t))

        print('\n'.join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
