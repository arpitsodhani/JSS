import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    l = int(data[1])
    r = int(data[2])
    x = int(data[3])
    hardness = [int(token) for token in data[4:n + 4]]
    return n, l, r, x, hardness

# Clause count_sets [Confidence: 0.40]
def count_sets(n, l, r, x, hardness):
    total = 0
    for mask in range(1, 1 << n):
        chosen = 0
        summed = 0
        low = 0
        high = 0
        for i in range(n):
            if mask & (1 << i):
                value = hardness[i]
                summed += value
                if chosen == 0 or value < low:
                    low = value
                if chosen == 0 or value > high:
                    high = value
                chosen += 1
        if chosen >= 2 and l <= summed <= r and high - low >= x:
            total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    n, l, r, x, hardness = read_input()
    sys.stdout.write(str(count_sets(n, l, r, x, hardness)) + "\n")


if __name__ == "__main__":
    main()

