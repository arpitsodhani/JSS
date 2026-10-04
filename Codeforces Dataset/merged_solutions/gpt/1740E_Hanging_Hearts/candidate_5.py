# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]

        parent = [0] * (n + 1)
        for i in range(2, n + 1):
            parent[i] = data[i - 2]

        f = [0] * (n + 1)
        g = [0] * (n + 1)
        cnt = [0] * (n + 1)
        sum_f = [0] * (n + 1)
        max_g = [0] * (n + 1)

        for u in range(n, 0, -1):
            if cnt[u] == 0:
                f[u] = 1
                g[u] = 1
            else:
                g[u] = max_g[u] + 1
                f[u] = max(sum_f[u], g[u])

            if u > 1:
                p = parent[u]
                cnt[p] += 1
                sum_f[p] += f[u]
                if g[u] > max_g[p]:
                    max_g[p] = g[u]

        print(f[1])

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
