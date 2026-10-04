import sys

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    m = nums[1]

    # CLAUSE: partition_by_weight
    grouped = ([], [], [])
    idx = 2
    for _ in range(n):
        w = nums[idx]
        c = nums[idx + 1]
        idx += 2
        grouped[w - 1].append(c)

    # CLAUSE: sort_value_tiers
    a, b, c = grouped
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # CLAUSE: build_prefix_sums
    pa = [0]
    for value in a:
        pa.append(pa[-1] + value)
    pb = [0]
    for value in b:
        pb.append(pb[-1] + value)
    pc = [0]
    for value in c:
        pc.append(pc[-1] + value)

    # CLAUSE: precompute_light_capacity_optima
    light_limit = min(m, len(a) + 2 * len(b))
    exact = [-1] * (light_limit + 1)
    exact[0] = 0
    for twos in range(min(len(b), light_limit // 2) + 1):
        val2 = pb[twos]
        base = 2 * twos
        ones_limit = min(len(a), light_limit - base)
        weights = range(base, base + ones_limit + 1)
        for weight, ones in zip(weights, range(ones_limit + 1)):
            candidate = val2 + pa[ones]
            if candidate > exact[weight]:
                exact[weight] = candidate
    best_light = [0] * (light_limit + 1)
    for weight in range(light_limit + 1):
        best_light[weight] = exact[weight]
        if weight and best_light[weight - 1] > best_light[weight]:
            best_light[weight] = best_light[weight - 1]

    # CLAUSE: scan_heavy_item_counts
    best_total = 0
    for used3 in range(0, min(m, 3 * len(c)) + 1, 3):
        count3 = used3 // 3
        gain3 = pc[count3]

        # CLAUSE: combine_capacity_profiles
        room = m - used3
        if room > light_limit:
            room = light_limit
        combined = gain3 + best_light[room]
        if combined > best_total:
            best_total = combined

    # CLAUSE: emit_maximum_value
    print(best_total)

if __name__ == "__main__":
    main()
