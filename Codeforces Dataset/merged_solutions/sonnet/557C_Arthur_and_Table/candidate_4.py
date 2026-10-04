import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return numbers[1:1 + n], numbers[1 + n:1 + 2 * n]


# --- clause: least_energy :: (lengths: list[int], costs: list[int]) -> int ---
def least_energy(lengths, costs):
    n = len(lengths)
    legs = sorted(zip(lengths, costs))
    total = sum(costs)
    counter = [0] * 201
    below_sum = 0
    below_count = 0
    best = total
    i = 0
    while i < n:
        j = i
        group = 0
        while j < n and legs[j][0] == legs[i][0]:
            group += legs[j][1]
            j += 1
        spend = total - below_sum - group
        allowed = j - i - 1
        drop = below_count - allowed
        price = 1
        while drop > 0:
            take = counter[price] if counter[price] < drop else drop
            spend += take * price
            drop -= take
            price += 1
        if spend < best:
            best = spend
        while i < j:
            counter[legs[i][1]] += 1
            below_sum += legs[i][1]
            below_count += 1
            i += 1
    return best


# --- clause: main :: () -> None ---
def main():
    lengths, costs = read_input()
    sys.stdout.write("%d\n" % least_energy(lengths, costs))


if __name__ == "__main__":
    main()
