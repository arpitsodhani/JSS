import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    c = int(data[pos])
    pos += 1
    cases = []
    for _ in range(c):
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases

# Clause divisor [Confidence: 1.00]
def divisor(x, y):
    while y:
        x, y = y, x % y
    return x

# Clause valid_log [Confidence: 1.00]
def valid_log(times):
    n = len(times)
    first = times[0]
    second = 0
    for value in times:
        if value % first:
            second = value
            break
    last = times[n - 1]
    if second == 0:
        if last // first == n:
            return "VALID"
        return "INVALID"
    for value in times:
        if value % first and value % second:
            return "INVALID"
    both = first // divisor(first, second) * second
    seen = last // first + last // second - last // both
    if seen == n:
        return "VALID"
    return "INVALID"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for case in read_input():
        out.append(valid_log(case))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

