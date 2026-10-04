# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    A, B, n = data[0], data[1], data[2]
    idx = 3
    out = []

    def height(i):
        return A + (i - 1) * B

    def segment_sum(l, r):
        cnt = r - l + 1
        return cnt * (height(l) + height(r)) // 2

    for _ in range(n):
        l, t, m = data[idx], data[idx + 1], data[idx + 2]
        idx += 3

        if height(l) > t:
            out.append("-1")
            continue

        lo, hi = l, l
        while height(hi) <= t and segment_sum(l, hi) <= m * t:
            hi *= 2

        ans = l
        while lo <= hi:
            mid = (lo + hi) // 2
            if height(mid) <= t and segment_sum(l, mid) <= m * t:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
