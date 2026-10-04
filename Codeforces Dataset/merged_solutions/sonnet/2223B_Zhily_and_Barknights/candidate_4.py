# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 998244353

class RatioRecord:
    __slots__ = ("numerator", "denominator", "count")

    def __init__(self, numerator, denominator, count):
        self.numerator = numerator
        self.denominator = denominator
        self.count = count

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

# CLAUSE: solve_logic
def lower_weight(numerators, denominators, prefix, x, y):
    left = 0
    right = len(numerators)
    while left < right:
        middle = (left + right) // 2
        if numerators[middle] * y < denominators[middle] * x:
            left = middle + 1
        else:
            right = middle
    return prefix[left]

def solve_case(n, a, b):
    if n == 1:
        return 0

    b_freq = Counter(b)
    records = []
    for first_b, first_count in b_freq.items():
        for second_b, second_count in b_freq.items():
            count = first_count * second_count
            if first_b == second_b:
                count -= first_count
            if count:
                records.append(RatioRecord(second_b, first_b, count))

    records.sort()

    numerators = [record.numerator for record in records]
    denominators = [record.denominator for record in records]
    prefix = [0] * (len(records) + 1)
    for i in range(len(records)):
        prefix[i + 1] = (prefix[i] + records[i].count) % MOD

    freq_before = {}
    result = 0
    for current in a:
        for earlier, amount in freq_before.items():
            add = lower_weight(numerators, denominators, prefix, earlier, current)
            result = (result + amount * add) % MOD
        freq_before[current] = freq_before.get(current, 0) + 1

    return result * pow(n * (n - 1) % MOD, MOD - 2, MOD) % MOD

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    t = raw[ptr]
    ptr += 1
    result_lines = []

    for _ in range(t):
        n = raw[ptr]
        ptr += 1
        a = raw[ptr:ptr + n]
        ptr += n
        b = raw[ptr:ptr + n]
        ptr += n
        result_lines.append(str(solve_case(n, a, b)))

    sys.stdout.write("\n".join(result_lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
