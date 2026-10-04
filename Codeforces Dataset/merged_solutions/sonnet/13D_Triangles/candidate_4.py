# CLAUSE: setup_environment
import sys
from itertools import combinations

def orient(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def build_masks(red, blue):
    n = len(red)
    m = len(blue)
    full = (1 << m) - 1
    masks = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in combinations(range(n), 2):
        mask = 0
        a = red[i]
        b = red[j]
        for bit, point in enumerate(blue):
            if orient(a, b, point) > 0:
                mask |= 1 << bit
        masks[i][j] = mask
        masks[j][i] = full ^ mask
    return masks

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return

    n, m = nums[0], nums[1]
    pairs = [(nums[i], nums[i + 1]) for i in range(2, len(nums), 2)]
    red = pairs[:n]
    blue = pairs[n:n + m]

    if m == 0:
        print(n * (n - 1) * (n - 2) // 6)
        return

    masks = build_masks(red, blue)
    answer = 0

    for i, j, k in combinations(range(n), 3):
        if orient(red[i], red[j], red[k]) > 0:
            inside = masks[i][j] & masks[j][k] & masks[k][i]
        else:
            inside = masks[j][i] & masks[k][j] & masks[i][k]
        if not inside:
            answer += 1

    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
