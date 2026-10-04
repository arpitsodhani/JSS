import sys
MOD = 1000000007

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    cases = []
    for _ in range(t):
        n = int(data[idx])
        cases.append((n, data[idx + 1]))
        idx += 2
    return cases

# Clause expected_ops [Confidence: 1.00]
def expected_ops(n, bits):
    half = (MOD + 1) // 2
    total = 0
    for k in range(n - 1, 0, -1):
        if bits[k] == 49:
            total = (total + 1) * half % MOD
        else:
            total = total * half % MOD
    return (n - 1 + total) % MOD

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, bits in read_input():
        out.append(str(expected_ops(n, bits)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

