# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        cnt = [0] * 4

        for i in range(n):
            x = data[1 + 2 * i] // 2
            y = data[2 + 2 * i] // 2
            cnt[(x & 1) * 2 + (y & 1)] += 1

        ans = n * (n - 1) * (n - 2) // 6

        bad = cnt[0] * cnt[3] * (n - cnt[0] - cnt[3])
        bad += cnt[1] * cnt[2] * (n - cnt[1] - cnt[2])

        print(ans - bad)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
