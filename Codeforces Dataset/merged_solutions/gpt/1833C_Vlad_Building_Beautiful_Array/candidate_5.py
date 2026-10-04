# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            has_odd = any(x % 2 for x in a)
            has_even = any(x % 2 == 0 for x in a)

            if not has_odd or not has_even:
                ans.append("YES")
            else:
                ans.append("YES" if min(a) % 2 == 1 else "NO")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
