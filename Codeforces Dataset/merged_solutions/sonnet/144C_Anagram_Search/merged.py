import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0], data[1]

# Clause count_good [Confidence: 1.00]
def count_good(s, p):
    width = len(p)
    length = len(s)
    if width > length:
        return 0
    quota = [0] * 26
    for ch in p:
        quota[ch - 97] += 1
    over = 0
    tally = [0] * 26
    total = 0
    left = 0
    for right in range(length):
        ch = s[right]
        if ch != 63:
            k = ch - 97
            tally[k] += 1
            if tally[k] > quota[k]:
                over += 1
        if right - left + 1 > width:
            gone = s[left]
            if gone != 63:
                k = gone - 97
                if tally[k] > quota[k]:
                    over -= 1
                tally[k] -= 1
            left += 1
        if right - left + 1 == width and over == 0:
            total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    s, p = read_input()
    sys.stdout.write(str(count_good(s, p)) + "\n")


if __name__ == "__main__":
    main()

