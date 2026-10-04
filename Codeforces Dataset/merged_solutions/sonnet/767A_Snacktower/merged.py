import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_tower [Confidence: 1.00]
def build_tower(fallen):
    n = len(fallen)
    have = [False] * (n + 2)
    wanted = n
    collected = []
    for length_of in fallen:
        have[length_of] = True
        placed = []
        while wanted >= 1 and have[wanted]:
            placed.append(str(wanted))
            wanted -= 1
        collected.append(" ".join(placed))
    return collected

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("\n".join(build_tower(read_input())) + "\n")


if __name__ == "__main__":
    main()

