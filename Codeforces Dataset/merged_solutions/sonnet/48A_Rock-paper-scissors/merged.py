import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0], data[1], data[2]

# Clause beats [Confidence: 1.00]
def beats(attacker, target):
    if attacker == b"rock":
        return target == b"scissors"
    if attacker == b"paper":
        return target == b"rock"
    return target == b"paper"

# Clause find_winner [Confidence: 1.00]
def find_winner(f, m, s):
    if beats(f, m) and beats(f, s):
        return "F"
    if beats(m, f) and beats(m, s):
        return "M"
    if beats(s, f) and beats(s, m):
        return "S"
    return "?"

# Clause main [Confidence: 1.00]
def main():
    f, m, s = read_input()
    sys.stdout.write(find_winner(f, m, s) + "\n")


if __name__ == "__main__":
    main()

