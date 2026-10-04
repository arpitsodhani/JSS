import sys

def hypergeom_update(dp, total, take):
    max_alive = len(dp) - 1

    if take == 0:
        return dp[:]
    if take == total:
        new_dp = [0.0] * (max_alive + 1)
        new_dp[0] = 1.0
        return new_dp

    new_dp = [0.0] * (max_alive + 1)

    for alive, base_prob in enumerate(dp):
        if base_prob == 0.0:
            continue
        if alive == 0:
            new_dp[0] += base_prob
            continue

        low = max(0, take - (total - alive))
        high = min(alive, take)

        if low == high:
            new_dp[alive - low] += base_prob
            continue

        mode = ((take + 1) * (alive + 1)) // (total + 2)
        if mode < low:
            mode = low
        elif mode > high:
            mode = high

        vals = [(mode, 1.0)]
        weight_sum = 1.0

        weight = 1.0
        for chosen in range(mode - 1, low - 1, -1):
            weight *= (chosen + 1) * (total - alive - take + chosen + 1)
            weight /= (alive - chosen) * (take - chosen)
            vals.append((chosen, weight))
            weight_sum += weight

        weight = 1.0
        for chosen in range(mode + 1, high + 1):
            prev = chosen - 1
            weight *= (alive - prev) * (take - prev)
            weight /= chosen * (total - alive - take + chosen)
            vals.append((chosen, weight))
            weight_sum += weight

        scale = base_prob / weight_sum
        for chosen, weight in vals:
            new_dp[alive - chosen] += scale * weight

    return new_dp

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0

    n = data[idx]
    idx += 1

    pots = [0] + data[idx:idx + n]
    idx += n

    q = data[idx]
    idx += 1

    dp = [None] * (n + 1)
    empty_prob = [0.0] * (n + 1)

    expected = 0.0
    for i in range(1, n + 1):
        dp[i] = [0.0] * (pots[i] + 1)
        dp[i][pots[i]] = 1.0
        if pots[i] == 0:
            empty_prob[i] = 1.0
            expected += 1.0

    out = []

    for _ in range(q):
        u = data[idx]
        v = data[idx + 1]
        k = data[idx + 2]
        idx += 3

        old_empty = empty_prob[u]
        dp[u] = hypergeom_update(dp[u], pots[u], k)
        empty_prob[u] = dp[u][0]
        expected += empty_prob[u] - old_empty

        if u != v:
            pots[u] -= k
            pots[v] += k

        out.append(f"{expected:.12f}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
