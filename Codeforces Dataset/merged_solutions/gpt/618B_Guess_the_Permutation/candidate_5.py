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

        n = data[0]
        vals = data[1:]

        ans = []
        for i in range(n):
            row = vals[i * n:(i + 1) * n]
            ans.append(max(row) if row else 0)

        used = set(ans)
        missing = next((x for x in range(1, n + 1) if x not in used), 1)

        if n == 1:
            ans = [1]
        else:
            seen = set()
            for i, x in enumerate(ans):
                if x in seen:
                    ans[i] = missing
                    break
                seen.add(x)

        print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
