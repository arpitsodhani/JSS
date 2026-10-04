import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), int(data[1])

# Clause pick_dropped [Confidence: 1.00]
def pick_dropped(word, k):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    dropped = set()
    for ch, times in sorted(counts.items(), key=lambda row: row[1]):
        if times <= k:
            k -= times
            dropped.add(ch)
    return dropped

# Clause main [Confidence: 1.00]
def main():
    word, k = read_input()
    dropped = pick_dropped(word, k)
    kept = "".join(ch for ch in word if ch not in dropped)
    left = set(kept)
    sys.stdout.write("%d\n%s\n" % (len(left), kept))


if __name__ == "__main__":
    main()

