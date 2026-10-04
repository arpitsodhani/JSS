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

# Clause gcd_of [Confidence: 1.00]
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a

# Clause smallest_coprime [Confidence: 0.80]
def smallest_coprime(a):
    for x in range(2, 200):
        for entry in a:
            if gcd_of(entry, x) == 1:
                return x
    return -1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(smallest_coprime(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

