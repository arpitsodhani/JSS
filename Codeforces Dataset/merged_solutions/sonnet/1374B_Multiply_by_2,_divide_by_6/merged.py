import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[1 + i]) for i in range(t)]

# Clause moves_needed [Confidence: 0.60]
def moves_needed(n):
    twos = 0
    threes = 0
    while n % 2 == 0:
        n //= 2
        twos += 1
    while n % 3 == 0:
        n //= 3
        threes += 1
    if n != 1 or threes < twos:
        return -1
    return 2 * threes - twos

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(str(moves_needed(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

