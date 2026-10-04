# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().strip().split()
        t = int(data[0])
        ans = []

        for i in range(1, t + 1):
            s = data[i]
            moves = min(s.count('0'), s.count('1'))
            ans.append("DA" if moves % 2 else "NET")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
