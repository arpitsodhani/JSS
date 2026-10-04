# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def better(h, c, t, a, b):
    ka = (a - 1) // 2
    kb = (b - 1) // 2
    numa = abs((ka + 1) * h + ka * c - t * a)
    numb = abs((kb + 1) * h + kb * c - t * b)
    left = numa * b
    right = numb * a
    if left != right:
        return a if left < right else b
    return min(a, b)

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    ans = []
    idx = 1
    for _ in range(q):
        h, c, t = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        if t * 2 <= h + c:
            ans.append('2')
            continue
        den = 2 * t - h - c
        k = (h - t) // den
        best = 1
        for x in (k - 1, k, k + 1, k + 2):
            if x >= 0:
                cups = 2 * x + 1
                best = better(h, c, t, best, cups)
        ans.append(str(best))
    sys.stdout.write('\n'.join(ans))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
