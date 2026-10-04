import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause build_string [Confidence: 0.80]
def build_string(t):
    if t.count("0") == 0 or t.count("1") == 0:
        return t
    return "01" * len(t)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for t in read_input():
        collected.append(build_string(t))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

