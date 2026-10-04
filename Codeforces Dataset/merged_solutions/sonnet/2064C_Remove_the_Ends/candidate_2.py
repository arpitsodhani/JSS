# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = nums[p]
    p += 1
    out = []
    for _ in range(t):
        n = nums[p]
        p += 1
        arr = nums[p:p + n]
        p += n

        left = [0] * (n + 1)
        for i, x in enumerate(arr):
            left[i + 1] = left[i] + (x if x > 0 else 0)

        right = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = arr[i]
            right[i] = right[i + 1] + (-x if x < 0 else 0)

        ans = 0
        for i in range(n + 1):
            val = left[i] + right[i]
            if val > ans:
                ans = val
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
