import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]

# Clause word_masks [Confidence: 1.00]
def word_masks(words):
    parity = []
    present = []
    for word in words:
        odd = 0
        seen = 0
        for ch in word:
            bit = 1 << (ord(ch) - 97)
            odd ^= bit
            seen |= bit
        parity.append(odd)
        present.append(seen)
    return parity, present

# Clause count_nightmares [Confidence: 1.00]
def count_nightmares(parity, present):
    full = (1 << 26) - 1
    total = 0
    for missing in range(26):
        bit = 1 << missing
        target = full ^ bit
        seen = {}
        for index in range(len(parity)):
            if present[index] & bit:
                continue
            mask = parity[index]
            partner = mask ^ target
            total += seen.get(partner, 0)
            seen[mask] = seen.get(mask, 0) + 1
    return total

# Clause main [Confidence: 1.00]
def main():
    words = read_input()
    parity, present = word_masks(words)
    sys.stdout.write(str(count_nightmares(parity, present)) + "\n")


if __name__ == "__main__":
    main()

