import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 + 2 * i].decode() for i in range(t)]

# Clause choose_indices [Confidence: 0.80]
def choose_indices(s):
    ones = []
    zeros = []
    for i in range(len(s)):
        if s[i] == "1":
            ones.append(i + 1)
        else:
            zeros.append(i + 1)
    if len(ones) % 2 == 0:
        return ones
    if len(zeros) % 2 == 1:
        return zeros
    return None

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        picked = choose_indices(s)
        if picked is None:
            collected.append("-1")
        else:
            collected.append(str(len(picked)))
            collected.append(" ".join(map(str, picked)))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

