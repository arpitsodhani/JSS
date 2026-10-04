import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    return n, m, data[2:2 + 2 * n + 2 * m]

# Clause annotate [Confidence: 1.00]
def annotate(n, m, rest):
    names = {}
    for i in range(n):
        names[rest[2 * i + 1]] = rest[2 * i].decode()
    out = []
    base = 2 * n
    for i in range(m):
        command = rest[base + 2 * i].decode()
        target = rest[base + 2 * i + 1]
        out.append(command + " " + target.decode() + " #" + names[target[:-1]])
    return out

# Clause main [Confidence: 1.00]
def main():
    n, m, rest = read_input()
    sys.stdout.write("\n".join(annotate(n, m, rest)) + "\n")


if __name__ == "__main__":
    main()

