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

# Clause candies_eaten [Confidence: 1.00]
def candies_eaten(a):
    low = min(a)
    total = 0
    for element in a:
        total += element - low
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(candies_eaten(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

