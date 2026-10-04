# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        a = list(map(int, sys.stdin.read().split()))
        n, k = a[0], a[1]
        x = a[2:2 + n]

        ans = 0
        i = 0

        while i < n - 1:
            j = i
            while j + 1 < n and x[j + 1] - x[i] <= k:
                j += 1
            if j == i:
                print(-1)
                sys.exit()
            ans += 1
            i = j

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
