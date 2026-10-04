# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 998244353

class FractionItem:
    __slots__ = ("p", "q", "w")

    def __init__(self, p, q, w):
        self.p = p
        self.q = q
        self.w = w

    def __lt__(self, other):
        return self.p * other.q < other.p * self.q

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    tests = values[pos]
    pos += 1
    answers = []

    for _ in range(tests):
        n = values[pos]
        pos += 1
        a = values[pos:pos + n]
        pos += n
        b = values[pos:pos + n]
        pos += n

        if n < 2:
            answers.append("0")
            continue

        counts = Counter(b)
        items = list(counts.items())
        fractions = []

        for den, den_count in items:
            for num, num_count in items:
                if den == num:
                    weight = den_count * (den_count - 1)
                else:
                    weight = den_count * num_count
                if weight:
                    fractions.append(FractionItem(num, den, weight))

        fractions.sort()
        numerators = [item.p for item in fractions]
        denominators = [item.q for item in fractions]
        pref = [0]
        running = 0
        for item in fractions:
            running = (running + item.w) % MOD
            pref.append(running)

        def below(left_value, right_value):
            lo = 0
            hi = len(fractions)
            while lo < hi:
                mid = (lo + hi) >> 1
                if numerators[mid] * right_value < denominators[mid] * left_value:
                    lo = mid + 1
                else:
                    hi = mid
            return pref[lo]

        previous = Counter()
        total = 0
        for right_value in a:
            for left_value, amount in previous.items():
                total = (total + amount * below(left_value, right_value)) % MOD
            previous[right_value] += 1

        denominator = n * (n - 1) % MOD
        answers.append(str(total * pow(denominator, MOD - 2, MOD) % MOD))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
