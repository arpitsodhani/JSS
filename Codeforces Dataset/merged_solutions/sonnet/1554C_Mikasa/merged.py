import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause smallest_missing [Confidence: 0.80]
def smallest_missing(n, m):
    target = m + 1
    answer = 0
    for bit in range(30, -1, -1):
        here = (n >> bit) & 1
        want = (target >> bit) & 1
        if here == want:
            continue
        if want:
            answer |= 1 << bit
        else:
            break
    return answer

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n, m in read_input():
        lines.append(smallest_missing(n, m))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

