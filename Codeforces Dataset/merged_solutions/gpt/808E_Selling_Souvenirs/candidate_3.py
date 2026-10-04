import sys

def main():
    a = list(map(int, sys.stdin.buffer.read().split()))
    if not a:
        return
    n, m = a[:2]

    # CLAUSE: partition_by_weight
    w1 = []
    w2 = []
    w3 = []
    for w, c in zip(a[2::2], a[3::2]):
        if w == 1:
            w1.append(c)
        elif w == 2:
            w2.append(c)
        else:
            w3.append(c)

    # CLAUSE: sort_value_tiers
    w1.sort()
    w2.sort()
    w3.sort()

    # CLAUSE: build_prefix_sums
    p1 = [0]
    while w1:
        p1.append(p1[-1] + w1.pop())
    p2 = [0]
    while w2:
        p2.append(p2[-1] + w2.pop())
    p3 = [0]
    while w3:
        p3.append(p3[-1] + w3.pop())

    # CLAUSE: precompute_light_capacity_optima
    max_light = min(m, len(p1) - 1 + 2 * (len(p2) - 1))
    light = [0] * (max_light + 1)
    for j, sum2 in enumerate(p2):
        base_weight = 2 * j
        if base_weight > max_light:
            break
        room = max_light - base_weight
        upto1 = min(len(p1) - 1, room)
        for i in range(upto1 + 1):
            idx = base_weight + i
            s = sum2 + p1[i]
            if s > light[idx]:
                light[idx] = s
    running = 0
    for i, v in enumerate(light):
        if v > running:
            running = v
        else:
            light[i] = running

    # CLAUSE: scan_heavy_item_counts
    best = 0
    for k, sum3 in enumerate(p3):
        used = 3 * k
        if used > m:
            break

        # CLAUSE: combine_capacity_profiles
        rem = m - used
        rem = max_light if rem > max_light else rem
        total = sum3 + light[rem]
        best = total if total > best else best

    # CLAUSE: emit_maximum_value
    print(best)

if __name__ == "__main__":
    main()
