import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    digits = data[0].decode()
    k = int(data[1])
    return digits, k

# Clause fewest_deletions [Confidence: 1.00]
def fewest_deletions(digits, k):
    size = len(digits)
    target = 10 ** k
    best = size - 1
    for mask in range(1, 1 << size):
        kept = []
        for i in range(size):
            if mask & (1 << i):
                kept.append(digits[i])
        if len(kept) > 1 and kept[0] == "0":
            continue
        value = int("".join(kept))
        if value % target == 0:
            removed = size - len(kept)
            if removed < best:
                best = removed
    return best

# Clause main [Confidence: 1.00]
def main():
    digits, k = read_input()
    sys.stdout.write(str(fewest_deletions(digits, k)) + "\n")


if __name__ == "__main__":
    main()

