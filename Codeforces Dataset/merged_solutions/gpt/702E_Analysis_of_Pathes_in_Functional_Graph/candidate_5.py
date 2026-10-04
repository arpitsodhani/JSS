# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n = data[0]
            k = data[1]
            f = data[2:2 + n]
            w = data[2 + n:2 + 2 * n]

            cur = list(range(n))
            ans_sum = [0] * n
            inf = 10 ** 30
            ans_min = [inf] * n

            nxt = f[:]
            sm = w[:]
            mn = w[:]

            while k:
                if k & 1:
                    for i in range(n):
                        v = cur[i]
                        ans_sum[i] += sm[v]
                        if mn[v] < ans_min[i]:
                            ans_min[i] = mn[v]
                        cur[i] = nxt[v]

                new_nxt = [0] * n
                new_sm = [0] * n
                new_mn = [0] * n

                for i in range(n):
                    v = nxt[i]
                    new_nxt[i] = nxt[v]
                    new_sm[i] = sm[i] + sm[v]
                    new_mn[i] = mn[i] if mn[i] < mn[v] else mn[v]

                nxt, sm, mn = new_nxt, new_sm, new_mn
                k >>= 1

            out = []
            for i in range(n):
                out.append(f"{ans_sum[i]} {0 if ans_min[i] == inf else ans_min[i]}")
            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
