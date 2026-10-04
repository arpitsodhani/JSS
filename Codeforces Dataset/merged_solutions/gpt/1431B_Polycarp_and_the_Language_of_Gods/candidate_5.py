# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().strip().split()
        if not data:
            sys.exit()

        t = int(data[0])
        ans = []

        for i in range(1, t + 1):
            s = data[i]
            res = 0
            run = 0

            for ch in s:
                if ch == 'w':
                    res += 1 + run // 2
                    run = 0
                else:
                    run += 1

            res += run // 2
            ans.append(str(res))

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
