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
        prefix = [int(token) for token in data[pos:pos + n]]
        pos += n
        suffix = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, prefix, suffix))
    return cases

# Clause divisor [Confidence: 0.80]
def divisor(x, y):
    while y:
        x, y = y, x % y
    return x

# Clause feasible [Confidence: 1.00]
def feasible(n, prefix, suffix):
    guess = [0] * n
    for i in range(n):
        common = divisor(prefix[i], suffix[i])
        guess[i] = prefix[i] // common * suffix[i]
    running = 0
    for i in range(n):
        running = divisor(running, guess[i])
        if running != prefix[i]:
            return "NO"
    running = 0
    for i in range(n - 1, -1, -1):
        running = divisor(running, guess[i])
        if running != suffix[i]:
            return "NO"
    return "YES"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, prefix, suffix in read_input():
        out.append(feasible(n, prefix, suffix))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

