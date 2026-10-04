# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n, k = data[0], data[1]
        a = data[2:2 + n]

        a.sort()

        for i in range(n):
            if k > 0 and a[i] < 0:
                a[i] = -a[i]
                k -= 1

        total = sum(a)

        if k % 2 == 1:
            total -= 2 * min(a)

        print(total)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
