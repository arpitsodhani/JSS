# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from array import array

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n, m, T = data[0], data[1], data[2]
            edges = []
            p = 3
            for _ in range(m):
                u, v, w = data[p], data[p + 1], data[p + 2]
                edges.append((u, v, w))
                p += 3

            inf = 10 ** 30
            prev = [inf] * (n + 1)
            prev[1] = 0

            parents = [array('H', [0]) * (n + 1) for _ in range(n + 1)]
            best_len = 1

            for length in range(1, n):
                cur = [inf] * (n + 1)
                par = parents[length + 1]

                for u, v, w in edges:
                    val = prev[u] + w
                    if val < cur[v]:
                        cur[v] = val
                        par[v] = u

                if cur[n] <= T:
                    best_len = length + 1

                prev = cur

            path = []
            v = n
            length = best_len
            while length:
                path.append(v)
                v = parents[length][v]
                length -= 1

            path.reverse()
            print(best_len)
            print(*path)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
