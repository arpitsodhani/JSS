# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        if not data:
            sys.exit()

        d, n = data[0], data[1]
        a = data[2:2 + n]

        ans = 0
        clock = 1

        for days in a:
            for day in range(1, days + 1):
                if clock != day:
                    add = (day - clock) % d
                    ans += add
                    clock = day
                clock += 1
                if clock > d:
                    clock = 1

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
