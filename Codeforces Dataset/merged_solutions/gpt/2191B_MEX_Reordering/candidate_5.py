# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            s = set(a)
            mex = 0
            while mex in s:
                mex += 1

            if mex == 0:
                ans.append("YES" if n == 1 else "NO")
            else:
                ok = any(a.count(x) == 1 for x in range(mex))
                ans.append("YES" if ok else "NO")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
