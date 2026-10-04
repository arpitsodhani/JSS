import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause best_total [Confidence: 1.00]
def best_total(n, a):
    best_minus = -a[0]
    best_plus = a[0]
    total = 0
    for i in range(1, n + 1):
        value = a[i - 1]
        first = best_minus + value
        second = best_plus - value
        total = first if first > second else second
        if i < n:
            nxt = a[i]
            if total - nxt > best_minus:
                best_minus = total - nxt
            if total + nxt > best_plus:
                best_plus = total + nxt
    return total

# Clause main [Confidence: 1.00]
def main():
    n, a = read_input()
    sys.stdout.write(str(best_total(n, a)) + "\n")


if __name__ == "__main__":
    main()

