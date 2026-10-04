import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# Clause kth_permutation [Confidence: 1.00]
def kth_permutation(n, k):
    cap = 2 * 10 ** 12
    total = 1
    steps = 0
    while steps < n - 1 and total <= cap:
        total *= 2
        steps += 1
    if total < k:
        return None
    result = [0] * n
    left = 0
    right = n - 1
    left_over = k
    for value in range(1, n + 1):
        if left == right:
            result[left] = value
            break
        width = right - left + 1
        half = 1
        for _ in range(width - 2):
            half *= 2
            if half > cap:
                break
        if left_over <= half:
            result[left] = value
            left += 1
        else:
            left_over -= half
            result[right] = value
            right -= 1
    return result

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k in read_input():
        order = kth_permutation(n, k)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

