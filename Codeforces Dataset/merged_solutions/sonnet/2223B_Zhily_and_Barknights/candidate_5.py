# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 998244353

class Ratio:
    __slots__ = ("num", "den", "weight")

    def __init__(self, num, den, weight):
        self.num = num
        self.den = den
        self.weight = weight

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

# CLAUSE: solve_logic
def prepare(b):
    frequencies = Counter(b)
    pairs = []
    for den, den_amount in frequencies.items():
        same_adjust = den_amount
        for num, num_amount in frequencies.items():
            weight = den_amount * num_amount
            if num == den:
                weight -= same_adjust
            if weight:
                pairs.append(Ratio(num, den, weight))

    pairs.sort()
    nums = []
    dens = []
    sums = [0]
    current = 0
    for pair in pairs:
        nums.append(pair.num)
        dens.append(pair.den)
        current += pair.weight
        current %= MOD
        sums.append(current)
    return nums, dens, sums

def query_prepared(nums, dens, sums, left_a, right_a):
    lo = 0
    hi = len(nums)
    while lo != hi:
        mid = (lo + hi) // 2
        if nums[mid] * right_a < dens[mid] * left_a:
            lo = mid + 1
        else:
            hi = mid
    return sums[lo]

def expected_value(n, a, b):
    nums, dens, sums = prepare(b)
    left_counts = Counter()
    total = 0

    for right_a in a:
        subtotal = 0
        for left_a, left_amount in left_counts.items():
            subtotal += left_amount * query_prepared(nums, dens, sums, left_a, right_a)
        total = (total + subtotal) % MOD
        left_counts[right_a] += 1

    return total * pow(n * (n - 1) % MOD, MOD - 2, MOD) % MOD

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    t = tokens[index]
    index += 1
    answers = []

    for _ in range(t):
        n = tokens[index]
        index += 1
        a = tokens[index:index + n]
        index += n
        b = tokens[index:index + n]
        index += n
        if n == 1:
            answers.append("0")
        else:
            answers.append(str(expected_value(n, a, b)))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
