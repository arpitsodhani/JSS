import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append(tuple(data[pos:pos + 6]))
        pos += 6
    return cases

# Clause attacked_from [Confidence: 1.00]
def attacked_from(a, b, x, y):
    spots = set()
    for dx, dy in ((a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)):
        spots.add((x + dx, y + dy))
    return spots

# Clause fork_count [Confidence: 0.80]
def fork_count(a, b, xk, yk, xq, yq):
    return len(attacked_from(a, b, xk, yk) & attacked_from(a, b, xq, yq))

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for a, b, xk, yk, xq, yq in read_input():
        collected.append(fork_count(a, b, xk, yk, xq, yq))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

