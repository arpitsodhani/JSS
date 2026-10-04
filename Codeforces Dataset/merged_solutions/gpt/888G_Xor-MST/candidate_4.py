# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_left

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n = data[0]
        a = sorted(data[1:1 + n])

        sys.setrecursionlimit(1_000_000)

        def split(l, r, b):
            x = ((a[l] >> (b + 1)) << (b + 1)) + (1 << b)
            return bisect_left(a, x, l, r)

        def min_xor(l1, r1, l2, r2, b):
            if b < 0:
                return 0
            m1 = split(l1, r1, b)
            m2 = split(l2, r2, b)

            ans = 1 << 60
            if l1 < m1 and l2 < m2:
                ans = min(ans, min_xor(l1, m1, l2, m2, b - 1))
            if m1 < r1 and m2 < r2:
                ans = min(ans, min_xor(m1, r1, m2, r2, b - 1))
            if ans != 1 << 60:
                return ans

            if l1 < m1 and m2 < r2:
                ans = min(ans, (1 << b) + min_xor(l1, m1, m2, r2, b - 1))
            if m1 < r1 and l2 < m2:
                ans = min(ans, (1 << b) + min_xor(m1, r1, l2, m2, b - 1))
            return ans

        def solve(l, r, b):
            if r - l <= 1 or b < 0:
                return 0
            m = split(l, r, b)
            if m == l or m == r:
                return solve(l, r, b - 1)
            return solve(l, m, b - 1) + solve(m, r, b - 1) + (1 << b) + min_xor(l, m, m, r, b - 1)

        print(solve(0, n, 30))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
