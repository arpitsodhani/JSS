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

# Clause can_eat [Confidence: 0.80]
def can_eat(a):
    if len(a) == 1:
        return a[0] == 1
    top = 0
    second = 0
    for element in a:
        if element > top:
            second = top
            top = element
        elif element > second:
            second = element
    return top - second <= 1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_eat(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

