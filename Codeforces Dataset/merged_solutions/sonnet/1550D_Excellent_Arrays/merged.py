# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 10**9 + 7

def build_factorials(limit):
    fact = [1] * (limit + 1)
    inv_fact = [1] * (limit + 1)
    for i in range(2, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    return fact, inv_fact

def choose(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD


# Clause solve_logic [Confidence: 0.80]
def excellent_arrays(n, l, r, factorial, inverse_factorial):
    half_down = n // 2
    half_up = n - half_down
    left_capacity = 1 - l
    right_capacity = r - n
    shared = min(left_capacity, right_capacity)

    balanced = combination(factorial, inverse_factorial, n, half_down)
    if half_down != half_up:
        balanced = 2 * balanced % MOD

    ans = shared % MOD * balanced % MOD
    end = shared + half_up

    for d in range(shared + 1, end + 1):
        fixed_from_left = d - left_capacity if d > left_capacity else 0
        fixed_from_right = d - right_capacity if d > right_capacity else 0
        open_slots = n - fixed_from_left - fixed_from_right

        if open_slots >= 0:
            add = combination(factorial, inverse_factorial, open_slots, half_down - fixed_from_left)
            if half_down != half_up:
                add += combination(factorial, inverse_factorial, open_slots, half_up - fixed_from_left)
            ans = (ans + add) % MOD

    return ans


# Clause finish_program [Confidence: 0.60]
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


