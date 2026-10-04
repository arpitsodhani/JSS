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

# Clause jump_cost [Confidence: 0.60]
def jump_cost(a):
    n = len(a)
    reach = 0
    while reach + 1 < n and a[reach + 1] == 1:
        reach += 1
    if reach == n - 1:
        return 0
    landing = n - 1
    while landing - 1 >= 0 and a[landing - 1] == 1:
        landing -= 1
    return landing - reach

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(jump_cost(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

