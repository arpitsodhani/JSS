import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k

# Clause color_count [Confidence: 1.00]
def color_count(n, k):
    count = 0
    reach = 1
    while reach < n:
        reach *= k
        count += 1
    return count

# Clause color_edges [Confidence: 1.00]
def color_edges(n, k):
    colors = []
    for a in range(n):
        for b in range(a + 1, n):
            high = a
            low = b
            level = 0
            while high != low:
                high //= k
                low //= k
                level += 1
            colors.append(level)
    return colors

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    count = color_count(n, k)
    colors = color_edges(n, k)
    answer = " ".join(map(str, colors))
    sys.stdout.write(str(count) + "\n" + answer + "\n")


if __name__ == "__main__":
    main()

