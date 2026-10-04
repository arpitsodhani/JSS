# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            k = data[idx + 2]
            idx += 3

            a = data[idx:idx + m]
            idx += m

            known = data[idx:idx + k]
            idx += k

            if k == n:
                ans.append("1" * m)
            elif k == n - 1:
                total = n * (n + 1) // 2
                missing = total - sum(known)
                ans.append("".join("1" if x == missing else "0" for x in a))
            else:
                ans.append("0" * m)

        sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
