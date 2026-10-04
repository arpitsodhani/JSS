# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def solve():
            input = sys.stdin.readline
            t = int(input())
            out = []
            for _ in range(t):
                n = int(input())
                s = input().strip()

                left = [0] * (n + 1)
                right = [0] * (n + 1)

                for i in range(n):
                    if s[i] == 'L':
                        left[i + 1] = right[i] + 1
                    else:
                        right[i + 1] = left[i] + 1

                ans = [0] * (n + 1)
                ans[0] = left[n] + 1

                for i in range(n - 1, -1, -1):
                    if s[i] == 'R':
                        left[i] = right[i + 1] + 1
                    else:
                        right[i] = left[i + 1] + 1

                for i in range(n + 1):
                    ans[i] = left[i] + right[i] + 1

                out.append(" ".join(map(str, ans)))

            print("\n".join(out))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
