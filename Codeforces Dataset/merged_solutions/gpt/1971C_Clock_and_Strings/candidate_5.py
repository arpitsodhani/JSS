# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        ans = []
        idx = 1

        for _ in range(t):
            a, b, c, d = data[idx:idx + 4]
            idx += 4

            if a > b:
                a, b = b, a

            c_inside = a < c < b
            d_inside = a < d < b

            ans.append("YES" if c_inside != d_inside else "NO")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
