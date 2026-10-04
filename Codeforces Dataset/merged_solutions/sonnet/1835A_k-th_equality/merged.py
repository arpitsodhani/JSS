import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2], data[pos + 3]))
        pos += 4
    return cases

# Clause kth_equality [Confidence: 1.00]
def kth_equality(a_len, b_len, c_len, k):
    low_a = 10 ** (a_len - 1)
    high_a = 10 ** a_len - 1
    low_b = 10 ** (b_len - 1)
    high_b = 10 ** b_len - 1
    low_c = 10 ** (c_len - 1)
    high_c = 10 ** c_len - 1
    for a in range(low_a, high_a + 1):
        first = low_b if low_b > low_c - a else low_c - a
        last = high_b if high_b < high_c - a else high_c - a
        if last < first:
            continue
        span = last - first + 1
        if k <= span:
            b = first + k - 1
            return "%d + %d = %d" % (a, b, a + b)
        k -= span
    return "-1"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a_len, b_len, c_len, k in read_input():
        out.append(kth_equality(a_len, b_len, c_len, k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

