import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause find_triple [Confidence: 0.80]
def find_triple(n):
    for x in range(1, 12):
        if x % 3 == 0:
            continue
        for y in range(x + 1, 24):
            if y % 3 == 0:
                continue
            z = n - x - y
            if z > y and z % 3:
                return x, y, z
    return None

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        triple = find_triple(n)
        if triple is None:
            collected.append("NO")
        else:
            collected.append("YES")
            collected.append("%d %d %d" % triple)
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

