# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        a = data[1:1 + n]

        suffix_min = [0] * n
        suffix_min[-1] = a[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(a[i], suffix_min[i + 1])

        ans = 1
        prefix_max = a[0]
        for i in range(n - 1):
            if a[i] > prefix_max:
                prefix_max = a[i]
            if prefix_max <= suffix_min[i + 1]:
                ans += 1

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
