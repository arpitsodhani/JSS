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

# Clause can_build [Confidence: 1.00]
def can_build(a):
    least_odd = -1
    least_even = -1
    for element in a:
        if element % 2:
            if least_odd < 0 or element < least_odd:
                least_odd = element
        else:
            if least_even < 0 or element < least_even:
                least_even = element
    if least_odd < 0 or least_even < 0:
        return True
    return least_odd < least_even

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_build(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

