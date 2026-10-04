# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def lower_bound(arr, value):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

def solve_case(ratings, problems, n, m):
    kevin = ratings[0]
    ratings.sort()
    penalties = []
    j = 0
    while j < m:
        d = problems[j]
        if d > kevin:
            cnt = n - lower_bound(ratings, d)
            if cnt > 0:
                penalties.append(cnt)
        j += 1
    penalties.sort(reverse=True)
    h = len(penalties)
    res = [0] * m
    k = 1
    while k <= m:
        total = m // k
        i = m % k
        if i > h:
            i = h
        while i < h:
            total += penalties[i]
            i += k
        res[k - 1] = str(total)
        k += 1
    return " ".join(res)

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    idx = 1
    out = []
    for _ in range(nums[0]):
        n = nums[idx]
        m = nums[idx + 1]
        idx += 2
        ratings = nums[idx:idx + n]
        idx += n
        problems = nums[idx:idx + m]
        idx += m
        out.append(solve_case(ratings, problems, n, m))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
