# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def prepare(limit):
    phi = list(range(limit + 1))
    prime = 2
    while prime <= limit:
        if phi[prime] == prime:
            multiple = prime
            while multiple <= limit:
                phi[multiple] -= phi[multiple] // prime
                multiple += prime
        prime += 1

    cumulative = [0] * (limit + 1)
    if limit >= 1:
        cumulative[1] = 1
    value = 2
    while value <= limit:
        cumulative[value] = cumulative[value - 1] + phi[value]
        value += 1

    costs = [[0] * (limit + 1) for _ in range(limit + 2)]
    right = 1
    while right <= limit:
        left = right
        while left > 0:
            costs[left][right] = costs[left + 1][right] + cumulative[right // left]
            left -= 1
        right += 1
    return costs

def compute_layer(previous, costs, n, layer):
    current = [0] * (n + 1)
    inf = 10 ** 31

    def divide(lo, hi, start, stop):
        if lo > hi:
            return
        mid = (lo + hi) // 2
        chosen = start
        best = inf
        end = min(stop, mid - 1)
        cut = start
        while cut <= end:
            trial = previous[cut] + costs[cut + 1][mid]
            if trial < best:
                best = trial
                chosen = cut
            cut += 1
        current[mid] = best
        divide(lo, mid - 1, start, chosen)
        divide(mid + 1, hi, chosen, stop)

    divide(layer, n, layer - 1, n - 1)
    return current

def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    if not numbers:
        return
    amount = numbers[0]
    cases = []
    limit = 0
    pos = 1
    for _ in range(amount):
        n = numbers[pos]
        k = numbers[pos + 1]
        pos += 2
        cases.append((n, k))
        if n > limit:
            limit = n

    costs = prepare(limit)
    result = []

    for n, k in cases:
        k = min(k, n)
        dp = [0] * (n + 1)
        base = costs[1]
        i = 1
        while i <= n:
            dp[i] = base[i]
            i += 1
        layer = 2
        while layer <= k:
            dp = compute_layer(dp, costs, n, layer)
            layer += 1
        result.append(str(dp[n]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
