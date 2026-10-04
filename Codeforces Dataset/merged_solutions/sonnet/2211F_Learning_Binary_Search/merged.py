# Clause setup_environment [Confidence: 0.80]
import sys

MOD = 676767677

def prepare(limit):
    fact = [1] * limit
    inv_fact = [1] * limit

    for i in range(1, limit):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact[limit - 1] = pow(fact[limit - 1], MOD - 2, MOD)

    for i in reversed(range(limit - 1)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    return fact, inv_fact

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    tests = []
    need = 5

    pos = 1
    for case_index in range(t):
        n = int(raw[pos])
        m = int(raw[pos + 1])
        pos += 2
        tests.append((n, m))
        need = max(need, n + m + 5)

    fact, inv_fact = prepare(need)

    def c(n, k):
        return 0 if k < 0 or k > n else fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    def segment_ways(slots, lower, upper):
        if lower > upper:
            return 0
        return c(upper - lower + slots, slots)


# Clause solve_logic [Confidence: 0.60]
    answers = []
    for n, m in pairs:
        memo = {}

        def solve(l, r, low, high):
            if l > r or low > high:
                return 0, 0
            key = (l, r, low, high)
            saved = memo.get(key)
            if saved is not None:
                return saved
            if l == r:
                val = (high - low + 1) % MOD
                memo[key] = (val, val)
                return val, val

            mid = (l + r) // 2
            total = 0
            distinct = 0
            left_len = mid - l
            right_len = r - mid

            for value in range(low, high + 1):
                left_count = count_arrays(left_len, low, value)
                right_count = count_arrays(right_len, value, high)
                ways = left_count * right_count % MOD
                total = (total + ways) % MOD
                distinct = (distinct + ways) % MOD

                if value > low and left_len:
                    left_total, left_distinct = solve(l, mid - 1, low, value - 1)
                    total = (total + right_count * (left_total + left_distinct)) % MOD
                    distinct = (distinct + right_count * left_distinct) % MOD

                if value < high and right_len:
                    right_total, right_distinct = solve(mid + 1, r, value + 1, high)
                    total = (total + left_count * (right_total + right_distinct)) % MOD
                    distinct = (distinct + left_count * right_distinct) % MOD

            memo[key] = (total, distinct)
            return total, distinct

        ans, _ = solve(1, n, 1, m)
        answers.append(str(ans))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()


