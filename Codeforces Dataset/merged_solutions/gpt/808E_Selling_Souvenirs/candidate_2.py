import sys

def prefix(values):
    out = [0]
    total = 0
    for x in values:
        total += x
        out.append(total)
    return out

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return
    n = tokens[0]
    m = tokens[1]

    # CLAUSE: partition_by_weight
    by_weight = {1: [], 2: [], 3: []}
    for i in range(n):
        w = tokens[2 + 2 * i]
        c = tokens[3 + 2 * i]
        by_weight[w].append(c)

    # CLAUSE: sort_value_tiers
    for w in (1, 2, 3):
        by_weight[w].sort(reverse=True)

    # CLAUSE: build_prefix_sums
    pref = {
        1: prefix(by_weight[1]),
        2: prefix(by_weight[2]),
        3: prefix(by_weight[3]),
    }

    # CLAUSE: precompute_light_capacity_optima
    light_cap = min(m, len(by_weight[1]) + 2 * len(by_weight[2]))
    best = [0] * (light_cap + 1)
    for cap in range(light_cap + 1):
        low_twos = max(0, (cap - len(by_weight[1]) + 1) // 2)
        high_twos = min(len(by_weight[2]), cap // 2)
        cur = 0
        for cnt2 in range(low_twos, high_twos + 1):
            cnt1 = min(len(by_weight[1]), cap - 2 * cnt2)
            value = pref[2][cnt2] + pref[1][cnt1]
            if value > cur:
                cur = value
        best[cap] = cur

    # CLAUSE: scan_heavy_item_counts
    ans = 0
    heavy_count = 0
    while heavy_count < len(pref[3]) and heavy_count * 3 <= m:
        value3 = pref[3][heavy_count]

        # CLAUSE: combine_capacity_profiles
        remaining = m - 3 * heavy_count
        if remaining >= light_cap:
            value = value3 + best[light_cap]
        else:
            value = value3 + best[remaining]
        if value > ans:
            ans = value
        heavy_count += 1

    # CLAUSE: emit_maximum_value
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()
