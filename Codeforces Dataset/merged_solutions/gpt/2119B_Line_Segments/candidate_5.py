# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            px, py, qx, qy = data[idx:idx + 4]
            idx += 4
            a = data[idx:idx + n]
            idx += n

            s = sum(a)
            m = max(a) if a else 0
            low = max(0, 2 * m - s)
            dx = px - qx
            dy = py - qy
            d2 = dx * dx + dy * dy

            if low * low <= d2 <= s * s:
                ans.append("Yes")
            else:
                ans.append("No")

        sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
