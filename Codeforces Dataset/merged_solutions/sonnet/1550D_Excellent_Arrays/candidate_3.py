# CLAUSE: setup_environment
import sys

MOD = 1000000007

def prepare(limit):
    fact = [1] * (limit + 1)
    inverse = [0] * (limit + 1)
    inv_fact = [1] * (limit + 1)

    if limit >= 1:
        inverse[1] = 1

    for value in range(1, limit + 1):
        fact[value] = fact[value - 1] * value % MOD
        if value > 1:
            inverse[value] = MOD - (MOD // value) * inverse[MOD % value] % MOD
        inv_fact[value] = inv_fact[value - 1] * inverse[value] % MOD

    return fact, inv_fact

def ncr(n, r, fact, inv_fact):
    return 0 if r < 0 or r > n else fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# CLAUSE: solve_logic
def count_excellent(test, fact, inv_fact):
    n, l, r = test
    left = 1 - l
    right = r - n
    small = n // 2
    large = n - small
    same_side = min(left, right)

    base = ncr(n, small, fact, inv_fact)
    if small < large:
        base = (base + base) % MOD

    total = same_side % MOD * base % MOD
    shift = same_side + 1
    stop = same_side + large

    while shift <= stop:
        need_plus = shift - left
        need_minus = shift - right
        if need_plus < 0:
            need_plus = 0
        if need_minus < 0:
            need_minus = 0

        remaining = n - need_plus - need_minus
        if remaining >= 0:
            total = (total + ncr(remaining, small - need_plus, fact, inv_fact)) % MOD
            if small < large:
                total = (total + ncr(remaining, large - need_plus, fact, inv_fact)) % MOD
        shift += 1

    return total

# CLAUSE: finish_program
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    amount = values[0]
    triples = [tuple(values[i:i + 3]) for i in range(1, 3 * amount + 1, 3)]
    limit = max(item[0] for item in triples) if triples else 0
    fact, inv_fact = prepare(limit)
    sys.stdout.write("\n".join(str(count_excellent(item, fact, inv_fact)) for item in triples))

if __name__ == "__main__":
    main()
