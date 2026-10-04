import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause fewest_steps [Confidence: 1.00]
def fewest_steps(powers):
    top = 1000000 + 25
    counts = [0] * (top + 2)
    for value in powers:
        counts[value] += 1
    steps = 0
    carry = 0
    for value in range(top + 1):
        here = counts[value] + carry
        steps += here & 1
        carry = here >> 1
    while carry:
        steps += carry & 1
        carry >>= 1
    return steps

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % fewest_steps(read_input()))


if __name__ == "__main__":
    main()

