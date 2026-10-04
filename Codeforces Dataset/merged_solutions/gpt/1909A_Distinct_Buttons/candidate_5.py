# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            pos_x = neg_x = pos_y = neg_y = False

            for _ in range(n):
                x = data[idx]
                y = data[idx + 1]
                idx += 2

                if x > 0:
                    pos_x = True
                if x < 0:
                    neg_x = True
                if y > 0:
                    pos_y = True
                if y < 0:
                    neg_y = True

            ans.append("NO" if pos_x and neg_x and pos_y and neg_y else "YES")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
