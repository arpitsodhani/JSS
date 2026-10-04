# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            it = iter(data)
            q = next(it)
            out = []
            INF = 10**30

            for _ in range(q):
                n = next(it)
                k = next(it)

                a = [next(it) for _ in range(k)]
                t = [next(it) for _ in range(k)]

                ans = [INF] * n
                for pos, temp in zip(a, t):
                    ans[pos - 1] = temp

                cur = INF
                for i in range(n):
                    cur = min(cur + 1, ans[i])
                    ans[i] = cur

                cur = INF
                for i in range(n - 1, -1, -1):
                    cur = min(cur + 1, ans[i])
                    ans[i] = min(ans[i], cur)

                out.append(" ".join(map(str, ans)))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
