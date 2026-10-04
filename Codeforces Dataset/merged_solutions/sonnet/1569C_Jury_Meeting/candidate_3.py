# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 998244353

# CLAUSE: solve_logic
def build_factorials(limit):
    values = [1] * (limit + 1)
    for x in range(1, limit + 1):
        values[x] = values[x - 1] * x % MOD
    return values

def answer_case(items, fact):
    freq = Counter(items)
    high = max(freq)

    if freq[high] > 1:
        return fact[len(items)]

    below = high - 1
    if below not in freq:
        return 0

    cnt = freq[below]
    return (fact[len(items)] - fact[len(items)] * pow(cnt + 1, MOD - 2, MOD)) % MOD

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    at = 1
    tests = []
    biggest = 0

    for _ in range(t):
        n = nums[at]
        at += 1
        cur = nums[at:at + n]
        at += n
        tests.append(cur)
        biggest = max(biggest, n)

    fact = build_factorials(biggest)
    sys.stdout.write("\n".join(str(answer_case(cur, fact)) for cur in tests))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
