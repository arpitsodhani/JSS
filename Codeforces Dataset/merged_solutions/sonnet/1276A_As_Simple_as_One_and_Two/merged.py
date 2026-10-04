import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause pick_positions [Confidence: 0.80]
def pick_positions(s):
    picked = []
    i = 0
    n = len(s)
    while i < n:
        if s[i:i + 5] == "twone":
            picked.append(i + 3)
            i += 5
        elif s[i:i + 3] == "one":
            picked.append(i + 2)
            i += 3
        elif s[i:i + 3] == "two":
            picked.append(i + 2)
            i += 3
        else:
            i += 1
    return picked

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        picked = pick_positions(s)
        collected.append(str(len(picked)))
        collected.append(" ".join(str(p) for p in picked))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

