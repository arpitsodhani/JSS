# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        a, b, c, m = map(int, input().split())

        z = max(c, m)
        if z > min(2 * c, 2 * m):
            print(-1)
            exit()

        y = max(b, 2 * m + 1, z + 1)
        if y > 2 * b:
            print(-1)
            exit()

        x = max(a, y + 1)
        if x > 2 * a:
            print(-1)
            exit()

        print(x)
        print(y)
        print(z)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
