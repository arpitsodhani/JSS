import sys
from itertools import accumulate

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]

    # CLAUSE: partition_by_weight
    buckets = [[], [], [], []]
    p = 2
    for _ in range(n):
        w = data[p]
        c = data[p + 1]
        p += 2
        buckets[w].append(c)

    # CLAUSE: sort_value_tiers
    ones = sorted(buckets[1], reverse=True)
    twos = sorted(buckets[2], reverse=True)
    threes = sorted(buckets[3], reverse=True)

    # CLAUSE: build_prefix_sums
    pref1 = [0] + list(accumulate(ones))
    pref2 = [0] + list(accumulate(twos))
    pref3 = [0] + list(accumulate(threes))

    # CLAUSE: precompute_light_capacity_optima
    limit = min(m, len(ones) + 2 * len(twos))
    best_light = [0] * (limit + 1)
    for take2 in range(len(pref2)):
        used = 2 * take2
        if used > limit:
            break
        value2 = pref2[take2]
        max_take1 = min(len(ones), limit - used)
        for take1 in range(max_take1 + 1):
            total_w = used + take1
            val = value2 + pref1[take1]
            if val > best_light[total_w]:
                best_light[total_w] = val
    for cap in range(1, limit + 1):
        if best_light[cap - 1] > best_light[cap]:
            best_light[cap] = best_light[cap - 1]

    # CLAUSE: scan_heavy_item_counts
    answer = 0
    max_heavy = min(len(threes), m // 3)
    for take3 in range(max_heavy + 1):
        heavy_weight = 3 * take3
        heavy_value = pref3[take3]

        # CLAUSE: combine_capacity_profiles
        rest = m - heavy_weight
        if rest > limit:
            rest = limit
        candidate = heavy_value + best_light[rest]
        if candidate > answer:
            answer = candidate

    # CLAUSE: emit_maximum_value
    print(answer)

if __name__ == "__main__":
    main()
