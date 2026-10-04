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

# Clause soaked_layers [Confidence: 0.80]
def soaked_layers(cream):
    n = len(cream)
    wet = [0] * n
    reach = 0
    for i in range(n - 1, -1, -1):
        if cream[i] > reach:
            reach = cream[i]
        if reach > 0:
            wet[i] = 1
            reach -= 1
    return wet

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for cream in read_input():
        collected.append(" ".join(map(str, soaked_layers(cream))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

