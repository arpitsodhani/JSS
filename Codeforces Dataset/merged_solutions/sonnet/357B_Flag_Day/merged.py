import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    dances = []
    pos = 2
    for _ in range(m):
        dances.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return n, m, dances

# Clause assign_colors [Confidence: 0.80]
def assign_colors(n, dances):
    color = [0] * (n + 1)
    for trio in dances:
        taken = 0
        for dancer in trio:
            if color[dancer]:
                taken = color[dancer]
        spare = [c for c in (1, 2, 3) if c != taken]
        pick = 0
        for dancer in trio:
            if not color[dancer]:
                color[dancer] = spare[pick]
                pick += 1
    return color[1:]

# Clause main [Confidence: 1.00]
def main():
    n, m, dances = read_input()
    sys.stdout.write(" ".join(map(str, assign_colors(n, dances))) + "\n")


if __name__ == "__main__":
    main()

