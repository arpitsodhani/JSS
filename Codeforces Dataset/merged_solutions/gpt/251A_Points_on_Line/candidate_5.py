# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n, d = data[0], data[1]
        a = data[2:2 + n]

        ans = 0
        l = 0

        for r in range(n):
            while a[r] - a[l] > d:
                l += 1
            k = r - l
            if k >= 2:
                ans += k * (k - 1) // 2

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
