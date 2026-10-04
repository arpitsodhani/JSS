import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    melodies = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        melodies.append(data[pos:pos + n])
        pos += n
    return melodies

# Clause is_perfect [Confidence: 0.80]
def is_perfect(notes):
    for i in range(len(notes) - 1):
        gap = notes[i] - notes[i + 1]
        if gap < 0:
            gap = -gap
        if gap != 5 and gap != 7:
            return False
    return True

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for notes in read_input():
        collected.append("YES" if is_perfect(notes) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

