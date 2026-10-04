import sys
MOD = 1000000007

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    x = int(data[1])
    s = data[2]
    return n, x, s

# Clause base_matrix [Confidence: 1.00]
def base_matrix(n, s, letter):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        if a == 0 or a == n:
            table[a][a] = 2
        else:
            table[a][a] = 1
        if a < n and s[a] == letter:
            table[a][a + 1] = 1
    return table

# Clause multiply [Confidence: 1.00]
def multiply(n, left, right):
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        row = left[a]
        dest = out[a]
        for b in range(a, n + 1):
            value = row[b]
            if not value:
                continue
            other = right[b]
            for c in range(b, n + 1):
                if other[c]:
                    dest[c] = (dest[c] + value * other[c]) % MOD
    return out

# Clause count_subsequences [Confidence: 0.80]
def count_subsequences(n, x, s):
    zero = base_matrix(n, s, 48)
    one = base_matrix(n, s, 49)
    if x == 0:
        return zero[0][n] % MOD
    older = zero
    newer = one
    for _ in range(2, x + 1):
        older, newer = newer, multiply(n, newer, older)
    return newer[0][n] % MOD

# Clause main [Confidence: 1.00]
def main():
    n, x, s = read_input()
    sys.stdout.write(str(count_subsequences(n, x, s)) + "\n")


if __name__ == "__main__":
    main()

