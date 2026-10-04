import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_array [Confidence: 1.00]
def build_array(n):
    elements = list(range(n - 3))
    even = 0
    odd = 0
    for i in range(n - 3):
        if i % 2:
            odd ^= elements[i]
        else:
            even ^= elements[i]
    large = 1 << 28
    taller = 1 << 29
    if (n - 3) % 2:
        elements.append(large)
        elements.append(taller)
        elements.append(large ^ taller ^ even ^ odd)
    else:
        elements.append(large)
        elements.append(large ^ taller ^ even ^ odd)
        elements.append(taller)
    return elements

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

