# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        a = data[1:]

        if n < 2:
            print(0)
        else:
            best = 0
            cur1 = 0
            cur2 = 0

            for i in range(n - 1):
                d = abs(a[i] - a[i + 1])
                x = d if i % 2 == 0 else -d
                y = -x

                cur1 = max(x, cur1 + x)
                cur2 = max(y, cur2 + y)
                best = max(best, cur1, cur2)

            print(best)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
