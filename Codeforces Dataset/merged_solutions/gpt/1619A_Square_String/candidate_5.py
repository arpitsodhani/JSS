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

        t = int(data[0])
        ans = []

        for i in range(1, t + 1):
            s = data[i]
            n = len(s)
            if n % 2 == 0 and s[:n // 2] == s[n // 2:]:
                ans.append("YES")
            else:
                ans.append("NO")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
