import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause steps_needed [Confidence: 0.80]
def steps_needed(a):
    return max(a) - min(a)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for a in read_input():
        collected.append(steps_needed(a))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

