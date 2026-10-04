# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split()
        if not data:
            sys.exit()

        n = int(data[0])
        dp = [10**18] * 8
        dp[0] = 0

        idx = 1
        for _ in range(n):
            c = int(data[idx])
            s = data[idx + 1]
            idx += 2

            mask = 0
            for ch in s:
                if ch == 'A':
                    mask |= 1
                elif ch == 'B':
                    mask |= 2
                elif ch == 'C':
                    mask |= 4

            ndp = dp[:]
            for m in range(8):
                nm = m | mask
                if dp[m] + c < ndp[nm]:
                    ndp[nm] = dp[m] + c
            dp = ndp

        print(dp[7] if dp[7] < 10**18 else -1)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
