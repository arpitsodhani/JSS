import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return raw[1:1 + n], raw[1 + n:1 + 2 * n]


# --- clause: least_energy :: (lengths: list[int], costs: list[int]) -> int ---
def least_energy(lengths, costs):
    n = len(lengths)
    legs = sorted(zip(lengths, costs))
    running = 0
    for cost in costs:
        running += cost
    counter = [0] * 201
    below_sum = 0
    below_count = 0
    best = running
    i = 0
    while i < n:
        j = i
        group = 0
        while j < n and legs[j][0] == legs[i][0]:
            group += legs[j][1]
            j += 1
        keep = j - i
        above = running - below_sum - group
        spend = above
        left = below_count - (keep - 1)
        if left > 0:
            hit = 0
            price = 1
            while hit < left and price <= 200:
                take = counter[price]
                if take > left - hit:
                    take = left - hit
                spend += take * price
                hit += take
                price += 1
        if spend < best:
            best = spend
        for t in range(i, j):
            counter[legs[t][1]] += 1
            below_sum += legs[t][1]
            below_count += 1
        i = j
    return best


# --- clause: main :: () -> None ---
def main():
    lengths, costs = read_input()
    sys.stdout.write("%d\n" % least_energy(lengths, costs))


if __name__ == "__main__":
    main()
