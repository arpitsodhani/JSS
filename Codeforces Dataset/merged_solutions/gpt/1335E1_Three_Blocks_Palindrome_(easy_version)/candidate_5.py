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
            idx += 1
            arr = data[idx:idx + n]
            idx += n

            pos = {}
            for i, x in enumerate(arr):
                pos.setdefault(x, []).append(i)

            ans = 0
            all_positions = list(pos.values())

            for ps in all_positions:
                if len(ps) > ans:
                    ans = len(ps)

            for ps in all_positions:
                m = len(ps)
                for k in range(1, m // 2 + 1):
                    left = ps[k - 1]
                    right = ps[m - k]
                    best_mid = 0
                    for qs in all_positions:
                        cnt = bisect_left(qs, right) - bisect_left(qs, left + 1)
                        if cnt > best_mid:
                            best_mid = cnt
                    cur = 2 * k + best_mid
                    if cur > ans:
                        ans = cur

            out.append(str(ans))

        sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
