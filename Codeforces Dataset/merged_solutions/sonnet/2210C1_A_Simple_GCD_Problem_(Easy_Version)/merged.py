import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        values = [int(token) for token in data[pos:pos + n]]
        pos += 2 * n
        cases.append(values)
    return cases

# Clause divisor [Confidence: 0.80]
def divisor(x, y):
    while y:
        x, y = y, x % y
    return x

# Clause count_moves [Confidence: 1.00]
def count_moves(values):
    n = len(values)
    total = 0
    for i in range(n):
        need = 1
        if i > 0:
            left = divisor(values[i], values[i - 1])
            need = left
        if i + 1 < n:
            right = divisor(values[i], values[i + 1])
            need = need * right // divisor(need, right)
        if need != values[i]:
            total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for case in read_input():
        out.append(str(count_moves(case)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

