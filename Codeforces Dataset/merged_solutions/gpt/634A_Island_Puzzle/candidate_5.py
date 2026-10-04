# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n = data[0]
        a = data[1:1 + n]
        b = data[1 + n:1 + 2 * n]

        x = [v for v in a if v != 0]
        y = [v for v in b if v != 0]

        if n == 1:
            print("YES")
        else:
            s = x + x
            ok = False
            m = n - 1
            for i in range(m):
                if s[i:i + m] == y:
                    ok = True
                    break
            print("YES" if ok else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
