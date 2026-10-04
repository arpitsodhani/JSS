# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def possible(target, all_values, inc_values, inc_prefix, removed, need, budget, n):
    enough = n - bisect_left(all_values, target)
    if removed >= target:
        enough -= 1
    take = need - enough
    if take <= 0:
        return True
    left_count = bisect_left(inc_values, target)
    if left_count < take:
        return False
    cost = target * take - (inc_prefix[left_count] - inc_prefix[left_count - take])
    return cost <= budget

def solve_one(n, k, a, b):
    half = n // 2
    need = n - half
    pairs = sorted((x, i) for i, x in enumerate(a))
    sorted_a = [x for x, _ in pairs]
    rank = [0] * n
    for j, item in enumerate(pairs):
        rank[item[1]] = j

    best = 0
    for i in range(n):
        if b[i] == 1:
            median_index = half if rank[i] < half else half - 1
            value = a[i] + k + sorted_a[median_index]
            if value > best:
                best = value

    zero_values = [a[i] for i in range(n) if b[i] == 0]
    if zero_values:
        removed = max(zero_values)
        inc_values = sorted(a[i] for i in range(n) if b[i] == 1)
        inc_prefix = [0] * (len(inc_values) + 1)
        for i, x in enumerate(inc_values, 1):
            inc_prefix[i] = inc_prefix[i - 1] + x

        low = 0
        high = max(a) + k + 1
        while high - low > 1:
            mid = (low + high) // 2
            if possible(mid, sorted_a, inc_values, inc_prefix, removed, need, k, n):
                low = mid
            else:
                high = mid
        if removed + low > best:
            best = removed + low

    return best

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 1
    answers = []
    for _ in range(nums[0]):
        n, k = nums[ptr], nums[ptr + 1]
        ptr += 2
        a = nums[ptr:ptr + n]
        ptr += n
        b = nums[ptr:ptr + n]
        ptr += n
        answers.append(str(solve_one(n, k, a, b)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
