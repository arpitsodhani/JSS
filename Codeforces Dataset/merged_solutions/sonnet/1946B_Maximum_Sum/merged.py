import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause best_piece [Confidence: 1.00]
def best_piece(a):
    best = 0
    running = 0
    for value in a:
        running += value
        if running < 0:
            running = 0
        if running > best:
            best = running
    return best

# Clause grown_sum [Confidence: 1.00]
def grown_sum(k, a):
    mod = 1000000007
    piece = best_piece(a)
    return (sum(a) + piece * (pow(2, k, mod) - 1)) % mod

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, a in read_input():
        out.append(grown_sum(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

