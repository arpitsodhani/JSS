# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def can(k, segments):
    left = right = 0
    for l, r in segments:
        left -= k
        right += k
        if right < l or r < left:
            return False
        left = max(left, l)
        right = min(right, r)
    return True

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        segments = []
        hi = 0
        for _ in range(n):
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            segments.append((l, r))
            hi = max(hi, l, r)

        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid, segments):
                hi = mid
            else:
                lo = mid + 1

        ans.append(str(lo))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
