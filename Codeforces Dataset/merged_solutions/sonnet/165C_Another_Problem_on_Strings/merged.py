import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), data[1].decode()

# Clause count_substrings [Confidence: 1.00]
def count_substrings(k, s):
    spots = [-1]
    for i in range(len(s)):
        if s[i] == "1":
            spots.append(i)
    spots.append(len(s))
    ones = len(spots) - 2
    total = 0
    if k == 0:
        for i in range(len(spots) - 1):
            gap = spots[i + 1] - spots[i] - 1
            total += gap * (gap + 1) // 2
        return total
    for from_here in range(1, ones - k + 2):
        left = spots[from_here] - spots[from_here - 1]
        finish = spots[from_here + k] - spots[from_here + k - 1]
        total += left * finish
    return total

# Clause main [Confidence: 1.00]
def main():
    k, s = read_input()
    sys.stdout.write("%d\n" % count_substrings(k, s))


if __name__ == "__main__":
    main()

