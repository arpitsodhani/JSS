import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()

# Clause shortest_walk [Confidence: 1.00]
def shortest_walk(row):
    wanted = len(set(row))
    tally = {}
    have = 0
    best = len(row)
    left = 0
    for right in range(len(row)):
        ch = row[right]
        tally[ch] = tally.get(ch, 0) + 1
        if tally[ch] == 1:
            have += 1
        while have == wanted:
            if right - left + 1 < best:
                best = right - left + 1
            drop = row[left]
            tally[drop] -= 1
            if tally[drop] == 0:
                have -= 1
            left += 1
    return best

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % shortest_walk(read_input()))


if __name__ == "__main__":
    main()

