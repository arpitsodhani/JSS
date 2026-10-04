import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return tokens[1:1 + n], tokens[1 + n:1 + 2 * n]


# --- clause: least_energy :: (lengths: list[int], costs: list[int]) -> int ---
def least_energy(lengths, costs):
    n = len(lengths)
    legs = sorted(zip(lengths, costs))
    amount = 0
    for cost in costs:
        amount += cost
    counter = [0] * 201
    below_sum = 0
    below_count = 0
    best = amount
    i = 0
    while i < n:
        j = i
        group = 0
        while j < n and legs[j][0] == legs[i][0]:
            group += legs[j][1]
            j += 1
        keep = j - i
        above = amount - below_sum - group
        spend = above
        left = below_count - (keep - 1)
        if left > 0:
            found = 0
            price = 1
            while found < left and price <= 200:
                take = counter[price]
                if take > left - found:
                    take = left - found
                spend += take * price
                found += take
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
