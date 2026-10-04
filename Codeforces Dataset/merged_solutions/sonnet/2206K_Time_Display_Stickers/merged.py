import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        pos += 1
        cases.append(data[pos].decode())
        pos += 1
    return cases

# Clause enough_for [Confidence: 1.00]
def enough_for(counts, k):
    left = list(counts)
    zeros = left[0] if left[0] < k else k
    rest = k - zeros
    if left[1] < rest:
        return False
    left[0] -= zeros
    left[1] -= rest
    if left[0] + left[1] < rest:
        return False
    take = left[0] if left[0] < rest else rest
    left[0] -= take
    left[1] -= rest - take
    low = left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    if low < k:
        return False
    need = k
    for digit in range(6):
        used = left[digit] if left[digit] < need else need
        left[digit] -= used
        need -= used
    return sum(left) >= zeros + k

# Clause most_displays [Confidence: 1.00]
def most_displays(s):
    counts = [0] * 10
    for ch in s:
        counts[ord(ch) - 48] += 1
    low = 0
    high = len(s) // 4
    while low < high:
        middle = (low + high + 1) // 2
        if enough_for(counts, middle):
            low = middle
        else:
            high = middle - 1
    return low

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(str(most_displays(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

