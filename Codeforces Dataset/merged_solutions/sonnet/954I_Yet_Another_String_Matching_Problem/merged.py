import sys

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0], data[1]

# Clause conflict_masks [Confidence: 1.00]
def conflict_masks(s, t):
    n = len(s)
    m = len(t)
    width = n - m + 1
    w = 17
    zero = "0" * w
    one = zero[1:] + "1"

    def build(seq, ln, reverse):
        parts = [[zero] * ln for _ in range(6)]
        for j in range(ln):
            c = seq[j] - 97
            pos = (ln - 1 - j) if reverse else j
            parts[c][pos] = one
        return [int("".join(p[::-1]), 2) for p in parts]

    s_bits = build(s, n, False)
    t_bits = build(t, m, True)

    mask_slot = (1 << w) - 1
    masks = [0] * width
    start_bit = (m - 1) * w
    for first in range(6):
        if s_bits[first] == 0:
            continue
        for second in range(6):
            if first == second or t_bits[second] == 0:
                continue
            prod = s_bits[first] * t_bits[second]
            chunk = prod >> start_bit
            bit = 1 << (first * 6 + second)
            for k in range(width):
                if (chunk >> (k * w)) & mask_slot:
                    masks[k] |= bit
    return masks

# Clause distances [Confidence: 1.00]
def distances(masks):
    out = []
    for mask in masks:
        parent = [0, 1, 2, 3, 4, 5]
        merges = 0
        for first in range(6):
            for second in range(6):
                if first == second or not mask >> (first * 6 + second) & 1:
                    continue
                a = first
                while parent[a] != a:
                    a = parent[a]
                b = second
                while parent[b] != b:
                    b = parent[b]
                if a != b:
                    parent[a] = b
                    merges += 1
        out.append(str(merges))
    return out

# Clause main [Confidence: 0.60]
def main():
    s, t = read_input()
    sys.stdout.write(" ".join(distances(conflict_masks(s, t))) + "\n")


if __name__ == "__main__":
    main()

