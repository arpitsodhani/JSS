# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    data = sys.stdin.read().split()
    presses = [int(x) & 1 for x in data]
    masks = [
        0b000001011,
        0b000010111,
        0b000100110,
        0b001011001,
        0b010111010,
        0b100110100,
        0b011001000,
        0b111010000,
        0b110100000,
    ]

    state = 0b111111111
    for i, bit in enumerate(presses):
        if bit:
            state ^= masks[i]

    out = []
    for r in range(3):
        line = ""
        for c in range(3):
            pos = r * 3 + c
            line += str((state >> pos) & 1)
        out.append(line)

    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.80]
main()


