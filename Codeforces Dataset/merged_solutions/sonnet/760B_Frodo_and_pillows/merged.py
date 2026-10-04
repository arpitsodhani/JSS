import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    return n, m, k

# Clause side_pillows [Confidence: 1.00]
def side_pillows(beds, peak):
    slope = peak - 1
    if slope > beds:
        slope = beds
    if slope < 0:
        slope = 0
    total = slope * peak - slope * (slope + 1) // 2
    return total + (beds - slope)

# Clause most_pillows [Confidence: 1.00]
def most_pillows(n, m, k):
    low = 1
    high = m
    while low < high:
        mid = (low + high + 1) // 2
        need = mid + side_pillows(k - 1, mid) + side_pillows(n - k, mid)
        if need <= m:
            low = mid
        else:
            high = mid - 1
    return low

# Clause main [Confidence: 1.00]
def main():
    n, m, k = read_input()
    sys.stdout.write(str(most_pillows(n, m, k)) + "\n")


if __name__ == "__main__":
    main()

