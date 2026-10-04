# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        q = data[0]
        ans = []
        idx = 1

        for _ in range(q):
            n, s, t = data[idx], data[idx + 1], data[idx + 2]
            idx += 3
            ans.append(str(max(n - s, n - t) + 1))

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
