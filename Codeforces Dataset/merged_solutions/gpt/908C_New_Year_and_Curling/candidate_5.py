# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        data = list(map(float, sys.stdin.read().split()))
        n = int(data[0])
        r = data[1]
        x = data[2:2 + n]

        y = []
        for i in range(n):
            cur = r
            for j in range(i):
                dx = abs(x[i] - x[j])
                if dx <= 2 * r:
                    cur = max(cur, y[j] + math.sqrt((2 * r) ** 2 - dx ** 2))
            y.append(cur)

        print(*y)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
