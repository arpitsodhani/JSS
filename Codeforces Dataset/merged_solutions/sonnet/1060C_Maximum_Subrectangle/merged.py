import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + n + m]
    x = data[2 + n + m]
    return a, b, x

# Clause min_window_sums [Confidence: 1.00]
def min_window_sums(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    running = 0
    for i, value in enumerate(arr):
        running += value
        prefix[i + 1] = running
    best = [0] * (n + 1)
    for length in range(1, n + 1):
        best[length] = min(tail - head for head, tail in zip(prefix, prefix[length:]))
    return best

# Clause best_area [Confidence: 1.00]
def best_area(a, b, x):
    left = min_window_sums(a)
    right = min_window_sums(b)
    answer = 0
    for la in range(1, len(left)):
        if left[la] > x:
            break
        budget = x // left[la]
        lo = 1
        hi = len(right) - 1
        lb = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if right[mid] <= budget:
                lb = mid
                lo = mid + 1
            else:
                hi = mid - 1
        if lb >= 1:
            area = la * lb
            if area > answer:
                answer = area
    return answer

# Clause main [Confidence: 1.00]
def main():
    a, b, x = read_input()
    sys.stdout.write(str(best_area(a, b, x)) + "\n")


if __name__ == "__main__":
    main()

