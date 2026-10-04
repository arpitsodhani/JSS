import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((int(data[1 + 2 * i]), data[2 + 2 * i].decode()))
    return cases

# Clause final_length [Confidence: 1.00]
def final_length(x, s):
    mod = 1000000007
    band = [int(ch) for ch in s]
    size = len(band)
    length = size % mod
    for stride in range(1, x + 1):
        digit = band[stride - 1]
        if size < x and digit > 1:
            tail = band[stride:size]
            for _ in range(digit - 1):
                for value in tail:
                    band.append(value)
                    size += 1
                    if size >= x:
                        break
                if size >= x:
                    break
        length = (length + (digit - 1) * ((length - stride) % mod)) % mod
    return length % mod

# Clause main [Confidence: 1.00]
def main():
    out = []
    for x, s in read_input():
        out.append(final_length(x, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

