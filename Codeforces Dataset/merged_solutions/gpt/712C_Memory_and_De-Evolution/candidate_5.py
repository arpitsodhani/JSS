# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.read().split()))
            x, y = data[0], data[1]

            sides = [y, y, y]
            ans = 0

            while min(sides) < x:
                sides.sort()
                sides[0] = min(x, sides[1] + sides[2] - 1)
                ans += 1

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
