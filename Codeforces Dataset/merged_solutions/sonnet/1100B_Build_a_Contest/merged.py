import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    made = [int(token) for token in data[2:m + 2]]
    return n, m, made

# Clause round_flags [Confidence: 1.00]
def round_flags(n, m, made):
    counts = [0] * (n + 1)
    ready = 0
    out = []
    for value in made:
        counts[value] += 1
        if counts[value] == 1:
            ready += 1
        if ready == n:
            out.append("1")
            ready = 0
            for level in range(1, n + 1):
                counts[level] -= 1
                if counts[level] > 0:
                    ready += 1
        else:
            out.append("0")
    return "".join(out)

# Clause main [Confidence: 1.00]
def main():
    n, m, made = read_input()
    sys.stdout.write(round_flags(n, m, made) + "\n")


if __name__ == "__main__":
    main()

