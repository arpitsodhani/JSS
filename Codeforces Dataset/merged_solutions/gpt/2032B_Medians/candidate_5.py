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
        p = 1

        for _ in range(t):
            n = data[p]
            k = data[p + 1]
            p += 2

            if k == 1 and n == 1:
                ans.append("1")
                ans.append("1")
            elif k % 2 == 0 and 1 < k < n:
                ans.append("3")
                ans.append(f"1 {k} {k + 1}")
            else:
                ans.append("-1")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
