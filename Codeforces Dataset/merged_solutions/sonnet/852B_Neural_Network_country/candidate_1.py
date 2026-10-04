import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    layers = data[1]
    m = data[2]
    entry = data[3:3 + n]
    middle = data[3 + n:3 + 2 * n]
    exit_costs = data[3 + 2 * n:3 + 3 * n]
    return layers, m, entry, middle, exit_costs


# --- clause: histogram :: (values: list[int], m: int) -> list[int] ---
def histogram(values, m):
    counts = [0] * m
    for value in values:
        counts[value % m] += 1
    return counts


# --- clause: mix :: (left: list[int], right: list[int], m: int) -> list[int] ---
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


# --- clause: count_paths :: (layers: int, m: int, entry: list[int], middle: list[int], exit_costs: list[int]) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    layers, m, entry, middle, exit_costs = read_input()
    sys.stdout.write("%d\n" % count_paths(layers, m, entry, middle, exit_costs))


if __name__ == "__main__":
    main()
