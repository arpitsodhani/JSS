# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n = data[0]
        a = sorted(data[1:])

        ans = 0
        for i in range(n // 2):
            s = a[i] + a[n - 1 - i]
            ans += s * s

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
