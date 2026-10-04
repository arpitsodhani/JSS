# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        if not data:
            sys.exit()

        if len(data) % 4 == 1 and data[0] == (len(data) - 1) // 4:
            data = data[1:]

        ans = []
        for i in range(0, len(data), 4):
            n, m, r, c = data[i:i + 4]
            pos = (r - 1) * m + c
            total = n * m - pos + (n - r) * (m - 1)
            ans.append(str(total))

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
