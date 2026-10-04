import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    first = data[0].decode()
    second = data[1].decode()
    return first, second

# Clause build_tail [Confidence: 1.00]
def build_tail(counts):
    acc = []
    for j in range(26):
        if counts[j]:
            acc.append(chr(97 + j) * counts[j])
    return "".join(acc)

# Clause find_answer [Confidence: 1.00]
def find_answer(s, t):
    n = len(s)
    m = len(t)
    limit = min(n, m)
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] += 1
    matched = 0
    while matched < limit and counts[ord(t[matched]) - 97] > 0:
        counts[ord(t[matched]) - 97] -= 1
        matched += 1
    if n > m and matched == limit:
        return t[:m] + build_tail(counts)
    for i in range(matched, -1, -1):
        if i < matched:
            counts[ord(t[i]) - 97] += 1
        if i < limit:
            start = ord(t[i]) - 96
            for c in range(start, 26):
                if counts[c] > 0:
                    counts[c] -= 1
                    return t[:i] + chr(97 + c) + build_tail(counts)
    return "-1"

# Clause main [Confidence: 1.00]
def main():
    s, t = read_input()
    print(find_answer(s, t))


if __name__ == "__main__":
    main()

