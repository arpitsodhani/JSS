import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return data[1:1 + n], data[1 + n:1 + 2 * n]

# Clause without_gap [Confidence: 1.00]
def without_gap(row):
    return [element for element in row if element]

# Clause same_cycle [Confidence: 1.00]
def same_cycle(a, b):
    if not a:
        return True
    if len(a) != len(b):
        return False
    from_here = -1
    for i in range(len(b)):
        if b[i] == a[0]:
            from_here = i
            break
    if from_here < 0:
        return False
    for i in range(len(a)):
        if a[i] != b[(from_here + i) % len(b)]:
            return False
    return True

# Clause main [Confidence: 1.00]
def main():
    a, b = read_input()
    ok = same_cycle(without_gap(a), without_gap(b))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()

