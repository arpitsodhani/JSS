# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import deque

        def main():
            input = sys.stdin.readline
            t = int(input())
            out = []

            for _ in range(t):
                n, m = map(int, input().split())
                g = [[] for _ in range(n)]

                for _ in range(m):
                    i, j, c = input().split()
                    i = int(i) - 1
                    j = int(j) - 1
                    w = 1 if c == "imposter" else 0
                    g[i].append((j, w))
                    g[j].append((i, w))

                color = [-1] * n
                ans = 0
                ok = True

                for s in range(n):
                    if color[s] != -1:
                        continue

                    q = deque([s])
                    color[s] = 0
                    cnt = [1, 0]

                    while q and ok:
                        v = q.popleft()
                        for to, w in g[v]:
                            need = color[v] ^ w
                            if color[to] == -1:
                                color[to] = need
                                cnt[need] += 1
                                q.append(to)
                            elif color[to] != need:
                                ok = False
                                break

                    if not ok:
                        break

                    ans += max(cnt)

                out.append(str(ans if ok else -1))

            print("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
