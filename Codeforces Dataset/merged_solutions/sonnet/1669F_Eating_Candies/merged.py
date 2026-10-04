import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        weights = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, weights))
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(n, weights):
    best = 0
    left = 0
    right = n - 1
    left_sum = 0
    right_sum = 0
    while left <= right:
        if left_sum == right_sum:
            eaten = left + (n - 1 - right)
            if eaten > best:
                best = eaten
            left_sum += weights[left]
            left += 1
        elif left_sum < right_sum:
            left_sum += weights[left]
            left += 1
        else:
            right_sum += weights[right]
            right -= 1
    if left_sum == right_sum:
        eaten = left + (n - 1 - right)
        if eaten > best:
            best = eaten
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, weights in read_input():
        out.append(str(solve_case(n, weights)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

