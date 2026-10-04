# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def lonely_count(n):
            ans = n
            l = 2
            while l <= n:
                q = n // l
                r = n // q
                ans -= (r - l + 1) * (q - 1)
                l = r + 1
            return ans

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        t = data[0]
        out = []
        for i in range(1, t + 1):
            out.append(str(lonely_count(data[i])))
        print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
