# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def add_weighted_transition(target, alive, probability, total, take):
    low = max(0, take - (total - alive))
    high = min(alive, take)

    if alive == 0 or low == high:
        target[alive - low] = target.get(alive - low, 0.0) + probability
        return

    mode = ((take + 1) * (alive + 1)) // (total + 2)
    if mode < low:
        mode = low
    elif mode > high:
        mode = high

    picked = [mode]
    weight_by_pick = [1.0]
    normalizer = 1.0

    weight = 1.0
    for chosen in range(mode - 1, low - 1, -1):
        weight *= (chosen + 1) * (total - alive - take + chosen + 1)
        weight /= (alive - chosen) * (take - chosen)
        picked.append(chosen)
        weight_by_pick.append(weight)
        normalizer += weight

    weight = 1.0
    for chosen in range(mode + 1, high + 1):
        previous = chosen - 1
        weight *= (alive - previous) * (take - previous)
        weight /= chosen * (total - alive - take + chosen)
        picked.append(chosen)
        weight_by_pick.append(weight)
        normalizer += weight

    scale = probability / normalizer
    for index, chosen in enumerate(picked):
        remaining = alive - chosen
        target[remaining] = target.get(remaining, 0.0) + scale * weight_by_pick[index]

def update_sparse(dist, total, take):
    if take == 0:
        return dict(dist)
    if take == total:
        return {0: 1.0}

    nxt = {}
    for alive, probability in dist.items():
        if probability != 0.0:
            add_weighted_transition(nxt, alive, probability, total, take)
    return nxt

def main():
    raw = sys.stdin.buffer.read().split()
    p = 0
    n = int(raw[p])
    p += 1

    pots = [0]
    for _ in range(n):
        pots.append(int(raw[p]))
        p += 1

    q = int(raw[p])
    p += 1

    dp = [None] * (n + 1)
    empty = [0.0] * (n + 1)
    expected = 0.0

    for shelf in range(1, n + 1):
        dp[shelf] = {pots[shelf]: 1.0}
        if pots[shelf] == 0:
            empty[shelf] = 1.0
            expected += 1.0

    ans = []
    for _ in range(q):
        u = int(raw[p])
        v = int(raw[p + 1])
        k = int(raw[p + 2])
        p += 3

        old_empty = empty[u]
        dp[u] = update_sparse(dp[u], pots[u], k)
        empty[u] = dp[u].get(0, 0.0)
        expected += empty[u] - old_empty

        if u != v:
            pots[u] -= k
            pots[v] += k

        ans.append("{:.12f}".format(expected))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
