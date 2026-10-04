# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def try_build(s, parts, n):
            by_len = [[] for _ in range(n)]
            for i, t in enumerate(parts):
                by_len[len(t)].append(i)

            ans = [''] * len(parts)

            for l in range(1, n):
                i, j = by_len[l]
                p = s[:l]
                q = s[n - l:]

                a = parts[i]
                b = parts[j]

                if a == p and b == q:
                    ans[i] = 'P'
                    ans[j] = 'S'
                elif a == q and b == p:
                    ans[i] = 'S'
                    ans[j] = 'P'
                else:
                    return None

            return ''.join(ans)

        def main():
            data = sys.stdin.read().strip().split()
            n = int(data[0])
            parts = data[1:]

            longest = [x for x in parts if len(x) == n - 1]
            a, b = longest[0], longest[1]

            candidates = [a + b[-1], b + a[-1]]

            for s in candidates:
                res = try_build(s, parts, n)
                if res is not None:
                    print(res)
                    return

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
