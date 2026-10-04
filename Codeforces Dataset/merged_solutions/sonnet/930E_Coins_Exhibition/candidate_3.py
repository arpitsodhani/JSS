import sys
from collections import defaultdict

# CLAUSE: setup_environment
MOD = 10 ** 9 + 7
INV2 = (MOD + 1) // 2

# CLAUSE: solve_logic
def transform(a, b, length, left_zero, left_one, pref_zero, pref_one):
    if length <= 0:
        return a, b
    cut_a = pref_one[left_zero - 1] if left_zero else 0
    cut_b = pref_zero[left_one - 1] if left_one else 0
    doubled = pow(2, length, MOD)
    merged = (doubled * (a + b) - (doubled - 1) * (cut_a + cut_b)) % MOD
    return (merged + cut_b - cut_a) * INV2 % MOD, (merged - cut_b + cut_a) * INV2 % MOD

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return

    k = nums[0]
    n = nums[1]
    m = nums[2]
    p = 3

    need_zero = defaultdict(int)
    need_one = defaultdict(int)
    checkpoints = {k, k - 1}

    for _ in range(n):
        l, r = nums[p], nums[p + 1]
        p += 2
        if l > need_zero[r]:
            need_zero[r] = l
        checkpoints.add(r)
        checkpoints.add(l - 1)

    for _ in range(m):
        l, r = nums[p], nums[p + 1]
        p += 2
        if l > need_one[r]:
            need_one[r] = l
        checkpoints.add(r)
        checkpoints.add(l - 1)

    pref_zero = {0: 1}
    pref_one = {0: 1}
    cur_zero = 1
    cur_one = 1
    pos = 0
    min_zero = 0
    min_one = 0

    for x in sorted(v for v in checkpoints if 0 < v <= k):
        z = need_zero.get(x, 0)
        o = need_one.get(x, 0)
        if z or o:
            cur_zero, cur_one = transform(cur_zero, cur_one, x - 1 - pos, min_zero, min_one, pref_zero, pref_one)
            pos = x - 1
            if z > min_zero:
                min_zero = z
            if o > min_one:
                min_one = o
            cur_zero, cur_one = transform(cur_zero, cur_one, 1, min_zero, min_one, pref_zero, pref_one)
            pos = x
        else:
            cur_zero, cur_one = transform(cur_zero, cur_one, x - pos, min_zero, min_one, pref_zero, pref_one)
            pos = x
        pref_zero[x] = cur_zero
        pref_one[x] = cur_one

    sys.stdout.write(str((cur_zero + cur_one - pref_zero[k - 1] - pref_one[k - 1]) % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
