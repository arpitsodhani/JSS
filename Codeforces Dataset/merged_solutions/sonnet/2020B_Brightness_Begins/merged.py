import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause int_sqrt [Confidence: 1.00]
def int_sqrt(value):
    root = int(value ** 0.5)
    while root * root > value:
        root -= 1
    while (root + 1) * (root + 1) <= value:
        root += 1
    return root

# Clause smallest_n [Confidence: 0.80]
def smallest_n(k):
    floor_value = 1
    ceiling_value = 2 * k + 2
    while floor_value < ceiling_value:
        mid = (floor_value + ceiling_value) // 2
        if mid - int_sqrt(mid) >= k:
            ceiling_value = mid
        else:
            floor_value = mid + 1
    return floor_value

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k in read_input():
        out.append(smallest_n(k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

