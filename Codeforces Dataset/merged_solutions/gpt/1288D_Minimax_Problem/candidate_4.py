# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        input = sys.stdin.readline
        n, m = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(n)]

        def ok(x):
            pos = [-1] * (1 << m)
            for idx, row in enumerate(a):
                mask = 0
                for j, val in enumerate(row):
                    if val >= x:
                        mask |= 1 << j
                pos[mask] = idx

            full = (1 << m) - 1
            for i in range(1 << m):
                if pos[i] == -1:
                    continue
                for j in range(1 << m):
                    if pos[j] != -1 and (i | j) == full:
                        return pos[i], pos[j]
            return None

        lo, hi = 0, 10 ** 9 + 1
        ans = (0, 0)

        while hi - lo > 1:
            mid = (lo + hi) // 2
            res = ok(mid)
            if res is not None:
                lo = mid
                ans = res
            else:
                hi = mid

        res = ok(lo)
        if res is not None:
            ans = res

        print(ans[0] + 1, ans[1] + 1)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
