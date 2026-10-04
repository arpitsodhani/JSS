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

        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            k = data[idx]
            n = data[idx + 1]
            idx += 2

            ans = [1]
            cur = 1
            diff = 1

            while len(ans) < k:
                remaining_after = k - len(ans) - 1
                if cur + diff + remaining_after <= n:
                    cur += diff
                    diff += 1
                else:
                    cur += 1
                ans.append(cur)

            out.append(" ".join(map(str, ans)))

        print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
