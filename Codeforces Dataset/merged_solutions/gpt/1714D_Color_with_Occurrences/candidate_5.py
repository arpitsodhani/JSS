# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def solve():
            data = sys.stdin.read().split()
            it = iter(data)
            tc = int(next(it))
            out = []

            for _ in range(tc):
                t = next(it)
                n = int(next(it))
                s = [next(it) for _ in range(n)]
                m = len(t)

                ans = []
                covered = 0

                while covered < m:
                    best_end = covered
                    best_idx = -1
                    best_start = -1

                    for i, pat in enumerate(s):
                        lp = len(pat)
                        for st in range(max(0, covered - lp + 1), covered + 1):
                            if st + lp <= m and t.startswith(pat, st):
                                if st + lp > best_end:
                                    best_end = st + lp
                                    best_idx = i
                                    best_start = st

                    if best_idx == -1:
                        ans = None
                        break

                    ans.append((best_idx + 1, best_start + 1))
                    covered = best_end

                if ans is None:
                    out.append("-1")
                else:
                    out.append(str(len(ans)))
                    for x, y in ans:
                        out.append(f"{x} {y}")

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
