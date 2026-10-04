# CLAUSE: setup_environment
import sys

MOD = 676767677

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pairs = []
    p = 1
    limit = 1
    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        p += 2
        pairs.append((n, m))
        if n + m + 5 > limit:
            limit = n + m + 5

    fact = [1] * limit
    for i in range(1, limit):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * limit
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(limit - 2, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    def count_arrays(length, low, high):
        if length == 0:
            return 1
        if low > high:
            return 0
        return comb(high - low + length, length)

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
