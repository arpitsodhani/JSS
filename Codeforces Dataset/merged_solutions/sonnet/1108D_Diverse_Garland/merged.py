import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lamps = list(data[1].decode())
    return n, lamps

# Clause recolour [Confidence: 1.00]
def recolour(n, lamps):
    changed = 0
    for i in range(1, n):
        if lamps[i] != lamps[i - 1]:
            continue
        changed += 1
        for colour in "RGB":
            if colour == lamps[i - 1]:
                continue
            if i + 1 < n and colour == lamps[i + 1]:
                continue
            lamps[i] = colour
            break
    return changed

# Clause main [Confidence: 1.00]
def main():
    n, lamps = read_input()
    changed = recolour(n, lamps)
    sys.stdout.write(str(changed) + "\n" + "".join(lamps) + "\n")


if __name__ == "__main__":
    main()

