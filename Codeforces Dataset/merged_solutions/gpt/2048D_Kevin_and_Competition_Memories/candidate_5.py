# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from bisect import bisect_left

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            idx += 2

            a = data[idx:idx + n]
            idx += n
            b = data[idx:idx + m]
            idx += m

            kevin = a[0]
            a.sort()

            vals = []
            for x in b:
                if x <= kevin:
                    vals.append(0)
                else:
                    vals.append(n - bisect_left(a, x))

            vals.sort()

            ans = []
            for k in range(1, m + 1):
                total = 0
                q = m // k
                for pos in range(k - 1, q * k, k):
                    total += vals[pos] + 1
                ans.append(str(total))

            out.append(" ".join(ans))

        sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
