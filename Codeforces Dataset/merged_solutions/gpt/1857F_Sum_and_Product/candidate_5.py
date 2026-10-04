# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from math import isqrt
        from collections import Counter

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n
            cnt = Counter(a)
            q = data[idx]
            idx += 1

            ans = []
            for _ in range(q):
                x = data[idx]
                y = data[idx + 1]
                idx += 2

                d = x * x - 4 * y
                if d < 0:
                    ans.append("0")
                    continue

                s = isqrt(d)
                if s * s != d or (x + s) & 1:
                    ans.append("0")
                    continue

                u = (x + s) // 2
                v = (x - s) // 2

                if u == v:
                    c = cnt[u]
                    ans.append(str(c * (c - 1) // 2))
                else:
                    ans.append(str(cnt[u] * cnt[v]))

            out.append(" ".join(ans))

        sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
