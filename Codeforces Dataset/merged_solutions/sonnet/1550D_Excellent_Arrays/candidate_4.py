# CLAUSE: setup_environment
import sys

MOD = 10**9 + 7

class Combinations:
    def __init__(self, size):
        self.fact = [1] * (size + 1)
        self.inv_fact = [1] * (size + 1)

        for i in range(size):
            self.fact[i + 1] = self.fact[i] * (i + 1) % MOD

        self.inv_fact[size] = pow(self.fact[size], MOD - 2, MOD)

        for i in range(size, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % MOD

    def take(self, n, k):
        if 0 <= k <= n:
            return self.fact[n] * self.inv_fact[k] % MOD * self.inv_fact[n - k] % MOD
        return 0

# CLAUSE: solve_logic
def evaluate(n, l, r, comb):
    lower = n // 2
    upper = (n + 1) // 2
    left_room = 1 - l
    right_room = r - n
    center = left_room if left_room < right_room else right_room

    middle_choices = comb.take(n, lower)
    if lower != upper:
        middle_choices = middle_choices * 2 % MOD

    result = center * middle_choices % MOD

    for distance in range(center + 1, center + upper + 1):
        plus_fixed = distance - left_room
        minus_fixed = distance - right_room

        if plus_fixed < 0:
            plus_fixed = 0
        if minus_fixed < 0:
            minus_fixed = 0

        free_positions = n - plus_fixed - minus_fixed
        if free_positions < 0:
            continue

        result = (result + comb.take(free_positions, lower - plus_fixed)) % MOD
        if lower != upper:
            result = (result + comb.take(free_positions, upper - plus_fixed)) % MOD

    return result

# CLAUSE: finish_program
def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    cases = []
    largest = 0

    pos = 1
    for _ in range(t):
        n = int(raw[pos])
        l = int(raw[pos + 1])
        r = int(raw[pos + 2])
        pos += 3
        cases.append((n, l, r))
        largest = max(largest, n)

    comb = Combinations(largest)
    answers = []
    for n, l, r in cases:
        answers.append(str(evaluate(n, l, r, comb)))

    print("\n".join(answers))

if __name__ == "__main__":
    main()
