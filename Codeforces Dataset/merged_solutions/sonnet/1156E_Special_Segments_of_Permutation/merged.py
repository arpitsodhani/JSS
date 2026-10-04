import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values

# Clause greater_bounds [Confidence: 1.00]
def greater_bounds(n, values):
    right = [n] * n
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and values[stack[-1]] < values[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and values[stack[-1]] < values[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)
    return left, right

# Clause count_special [Confidence: 1.00]
def count_special(n, values, left, right):
    where = [0] * (n + 1)
    for i in range(n):
        where[values[i]] = i
    total = 0
    for i in range(n):
        low = left[i]
        high = right[i]
        peak = values[i]
        if i - low <= high - i:
            for l in range(low + 1, i):
                other = peak - values[l]
                if 1 <= other <= n:
                    r = where[other]
                    if i < r < high:
                        total += 1
        else:
            for r in range(i + 1, high):
                other = peak - values[r]
                if 1 <= other <= n:
                    l = where[other]
                    if low < l < i:
                        total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    left, right = greater_bounds(n, values)
    sys.stdout.write(str(count_special(n, values, left, right)) + "\n")


if __name__ == "__main__":
    main()

