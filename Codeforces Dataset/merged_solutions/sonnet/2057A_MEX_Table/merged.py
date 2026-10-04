import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause best_total [Confidence: 0.80]
def best_total(n, m):
    return (n if n > m else m) + 1

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n, m in read_input():
        collected.append(best_total(n, m))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

