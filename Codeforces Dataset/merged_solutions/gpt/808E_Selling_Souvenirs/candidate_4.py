import sys

def make_prefix(items):
    items.sort(reverse=True)
    pref = [0] * (len(items) + 1)
    for i, x in enumerate(items, 1):
        pref[i] = pref[i - 1] + x
    return pref

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return
    n, m = raw[0], raw[1]

    # CLAUSE: partition_by_weight
    parts = [[] for _ in range(4)]
    it = iter(raw[2:])
    for w, c in zip(it, it):
        parts[w].append(c)

    # CLAUSE: sort_value_tiers
    one_values = parts[1]
    two_values = parts[2]
    three_values = parts[3]

    # CLAUSE: build_prefix_sums
    one = make_prefix(one_values)
    two = make_prefix(two_values)
    three = make_prefix(three_values)

    # CLAUSE: precompute_light_capacity_optima
    cap = min(m, len(one) - 1 + 2 * (len(two) - 1))
    light_best = [0] * (cap + 1)
    for ones_taken in range(min(len(one) - 1, cap) + 1):
        light_best[ones_taken] = one[ones_taken]
    for twos_taken in range(1, min(len(two) - 1, cap // 2) + 1):
        weight2 = twos_taken + twos_taken
        value2 = two[twos_taken]
        most_ones = min(len(one) - 1, cap - weight2)
        row_end = weight2 + most_ones
        pos = weight2
        ones_taken = 0
        while pos <= row_end:
            val = value2 + one[ones_taken]
            if val > light_best[pos]:
                light_best[pos] = val
            pos += 1
            ones_taken += 1
    for i in range(1, cap + 1):
        light_best[i] = max(light_best[i], light_best[i - 1])

    # CLAUSE: scan_heavy_item_counts
    result = 0
    heavy_weight = 0
    heavy_taken = 0
    while heavy_taken <= len(three) - 1 and heavy_weight <= m:
        v3 = three[heavy_taken]

        # CLAUSE: combine_capacity_profiles
        rem_cap = m - heavy_weight
        light_cap = min(rem_cap, cap)
        result = max(result, v3 + light_best[light_cap])
        heavy_taken += 1
        heavy_weight += 3

    # CLAUSE: emit_maximum_value
    sys.stdout.write(f"{result}\n")

if __name__ == "__main__":
    main()
