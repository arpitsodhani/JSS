# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n, m = data[0], data[1]
        v = data[2:2 + n]

        ans = 0
        idx = 2 + n
        for _ in range(m):
            a = data[idx] - 1
            b = data[idx + 1] - 1
            idx += 2
            ans += min(v[a], v[b])

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
