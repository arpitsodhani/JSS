import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode()

# Clause can_share [Confidence: 0.80]
def can_share(k, s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in counts:
        if counts[ch] > k:
            return False
    return True

# Clause main [Confidence: 1.00]
def main():
    k, s = read_input()
    sys.stdout.write("YES\n" if can_share(k, s) else "NO\n")


if __name__ == "__main__":
    main()

