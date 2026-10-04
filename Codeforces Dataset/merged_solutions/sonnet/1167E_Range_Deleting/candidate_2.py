# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n, x = nums[0], nums[1]
    arr = nums[2:]

    inf = n + 1
    first = [inf] * (x + 3)
    last = [0] * (x + 3)

    for idx, val in enumerate(arr, 1):
        if first[val] == inf:
            first[val] = idx
        last[val] = idx

    pref_ok = [True] * (x + 3)
    pref_last = [0] * (x + 3)
    far = 0
    for val in range(1, x + 1):
        pref_ok[val] = pref_ok[val - 1] and far <= first[val]
        far = max(far, last[val])
        pref_last[val] = far

    suff_ok = [True] * (x + 4)
    suff_first = [inf] * (x + 4)
    near = inf
    for val in range(x, 0, -1):
        suff_ok[val] = suff_ok[val + 1] and last[val] <= near
        near = min(near, first[val])
        suff_first[val] = near

    ans = 0
    r = 1
    for l in range(1, x + 1):
        if not pref_ok[l - 1]:
            break
        if r < l:
            r = l
        while r <= x and (not suff_ok[r + 1] or pref_last[l - 1] > suff_first[r + 1]):
            r += 1
        if r <= x:
            ans += x - r + 1

    sys.stdout.write(str(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
