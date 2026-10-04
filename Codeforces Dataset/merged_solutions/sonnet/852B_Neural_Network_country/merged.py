import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    layers = data[1]
    m = data[2]
    entry = data[3:3 + n]
    middle = data[3 + n:3 + 2 * n]
    exit_costs = data[3 + 2 * n:3 + 3 * n]
    return layers, m, entry, middle, exit_costs

# Clause histogram [Confidence: 1.00]
def histogram(values, m):
    buckets = [0] * m
    for value in values:
        buckets[value % m] += 1
    return buckets

# Clause mix [Confidence: 1.00]
def mix(left, right, m):
    mod = 10 ** 9 + 7
    out = [0] * m
    for i in range(m):
        if left[i] == 0:
            continue
        for j in range(m):
            if right[j]:
                out[(i + j) % m] = (out[(i + j) % m] + left[i] * right[j]) % mod
    return out

# Clause count_paths [Confidence: 1.00]
def count_paths(layers, m, entry, middle, exit_costs):
    mod = 10 ** 9 + 7
    n = len(entry)
    head = histogram([entry[i] + middle[i] for i in range(n)], m)
    tail = histogram([exit_costs[i] + middle[i] for i in range(n)], m)
    step = histogram([2 * middle[i] for i in range(n)], m)
    inner = [0] * m
    inner[0] = 1
    power = layers - 2
    while power:
        if power % 2:
            inner = mix(inner, step, m)
        step = mix(step, step, m)
        power //= 2
    joined = mix(head, tail, m)
    total = 0
    for i in range(m):
        total = (total + joined[i] * inner[(m - i) % m]) % mod
    return total

# Clause main [Confidence: 1.00]
def main():
    layers, m, entry, middle, exit_costs = read_input()
    sys.stdout.write("%d\n" % count_paths(layers, m, entry, middle, exit_costs))


if __name__ == "__main__":
    main()

