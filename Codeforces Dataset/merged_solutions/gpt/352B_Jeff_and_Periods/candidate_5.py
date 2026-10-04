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

        n = data[0]
        a = data[1:1 + n]

        info = {}

        for i, x in enumerate(a, 1):
            if x not in info:
                info[x] = [i, 0, True, 1]
            else:
                last, diff, ok, count = info[x]
                cur_diff = i - last
                if count == 1:
                    diff = cur_diff
                elif diff != cur_diff:
                    ok = False
                info[x] = [i, diff, ok, count + 1]

        ans = []
        for x in sorted(info):
            last, diff, ok, count = info[x]
            if ok:
                ans.append((x, 0 if count == 1 else diff))

        print(len(ans))
        for x, d in ans:
            print(x, d)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
