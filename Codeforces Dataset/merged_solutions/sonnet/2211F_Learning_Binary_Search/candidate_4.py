# CLAUSE: setup_environment
import sys

MOD = 676767677

class Combinatorics:
    def __init__(self, size):
        self.fact = [1] * size
        for i in range(1, size):
            self.fact[i] = self.fact[i - 1] * i % MOD
        self.inv_fact = [1] * size
        self.inv_fact[-1] = pow(self.fact[-1], MOD - 2, MOD)
        for i in range(size - 2, -1, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % MOD

    def choose(self, n, k):
        if k < 0 or n < k:
            return 0
        return self.fact[n] * self.inv_fact[k] % MOD * self.inv_fact[n - k] % MOD

    def arrays(self, length, low, high):
        if low > high:
            return 0
        if length == 0:
            return 1
        return self.choose(high - low + length, length)

def parse_input():
    values = [int(x) for x in sys.stdin.buffer.read().split()]
    total = values[0]
    tests = []
    largest = 0
    at = 1
    for _ in range(total):
        n = values[at]
        m = values[at + 1]
        at += 2
        tests.append((n, m))
        largest = max(largest, n + m + 5)
    return tests, max(largest, 5)

# CLAUSE: solve_logic
def solve_case(n, m, comb):
    cache = {}

    def rec(l, r, lo, hi):
        if l > r or lo > hi:
            return 0, 0

        state = (l, r, lo, hi)
        if state in cache:
            return cache[state]

        if l == r:
            one = (hi - lo + 1) % MOD
            cache[state] = (one, one)
            return one, one

        mid = (l + r) // 2
        left_slots = mid - l
        right_slots = r - mid
        answer = 0
        distinct = 0

        left_choices = [comb.arrays(left_slots, lo, x) for x in range(lo, hi + 1)]
        right_choices = [comb.arrays(right_slots, x, hi) for x in range(lo, hi + 1)]

        for offset, current in enumerate(range(lo, hi + 1)):
            left_count = left_choices[offset]
            right_count = right_choices[offset]
            direct = left_count * right_count % MOD

            answer = (answer + direct) % MOD
            distinct = (distinct + direct) % MOD

            if left_slots != 0 and current != lo:
                sub_answer, sub_distinct = rec(l, mid - 1, lo, current - 1)
                answer = (answer + right_count * (sub_answer + sub_distinct)) % MOD
                distinct = (distinct + right_count * sub_distinct) % MOD

            if right_slots != 0 and current != hi:
                sub_answer, sub_distinct = rec(mid + 1, r, current + 1, hi)
                answer = (answer + left_count * (sub_answer + sub_distinct)) % MOD
                distinct = (distinct + left_count * sub_distinct) % MOD

        cache[state] = (answer, distinct)
        return answer, distinct

    result, unused = rec(1, n, 1, m)
    return result

def main():
    tests, limit = parse_input()
    comb = Combinatorics(limit)
    results = [str(solve_case(n, m, comb)) for n, m in tests]

# CLAUSE: finish_program
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
