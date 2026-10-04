# CLAUSE: setup_environment
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

# CLAUSE: solve_logic
    lines = []
    for n, m in tests:
        memo = {}

        def work(l, r, bounds):
            low, high = bounds
            if l > r or low > high:
                return 0, 0

            key = (l, r, low, high)
            value = memo.get(key)
            if value is not None:
                return value

            if l == r:
                amount = (high - low + 1) % MOD
                value = (amount, amount)
                memo[key] = value
                return value

            mid = (l + r) // 2
            before = mid - l
            after = r - mid
            total = 0
            unique = 0

            for chosen in range(low, high + 1):
                ways_before = segment_ways(before, low, chosen)
                ways_after = segment_ways(after, chosen, high)

                hit_here = ways_before * ways_after % MOD
                total = (total + hit_here) % MOD
                unique = (unique + hit_here) % MOD

                if before > 0 and chosen - 1 >= low:
                    subtotal, subunique = work(l, mid - 1, (low, chosen - 1))
                    total = (total + ways_after * (subtotal + subunique)) % MOD
                    unique = (unique + ways_after * subunique) % MOD

                if after > 0 and chosen + 1 <= high:
                    subtotal, subunique = work(mid + 1, r, (chosen + 1, high))
                    total = (total + ways_before * (subtotal + subunique)) % MOD
                    unique = (unique + ways_before * subunique) % MOD

            value = (total, unique)
            memo[key] = value
            return value

        answer, ignored = work(1, n, (1, m))
        lines.append(str(answer))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
