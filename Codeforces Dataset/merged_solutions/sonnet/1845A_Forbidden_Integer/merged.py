import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
    return cases

# Clause build_sum [Confidence: 0.80]
def build_sum(n, k, x):
    if x != 1:
        return [1] * n
    if k < 2:
        return None
    if n % 2 == 0:
        return [2] * (n // 2)
    if k < 3:
        return None
    return [3] + [2] * ((n - 3) // 2)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n, k, x in read_input():
        parts = build_sum(n, k, x)
        if parts is None:
            collected.append("NO")
        else:
            collected.append("YES")
            collected.append(str(len(parts)))
            collected.append(" ".join(map(str, parts)))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

