import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        a = int(data[pos])
        b = int(data[pos + 1])
        n = int(data[pos + 2])
        pos += 3
        tools = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((a, b, tools))
    return cases

# Clause survival_time [Confidence: 0.60]
def survival_time(a, b, tools):
    total = b
    cap = a - 1
    for gain in tools:
        total += cap if cap < gain else gain
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b, tools in read_input():
        out.append(str(survival_time(a, b, tools)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

