import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, data[2].decode()

# Clause smallest_value [Confidence: 0.80]
def smallest_value(n, k, s):
    if n == 1:
        return "0" if k > 0 else s
    out = list(s)
    spare = k
    if spare > 0 and out[0] != "1":
        out[0] = "1"
        spare -= 1
    for position in range(1, n):
        if spare <= 0:
            break
        if out[position] > "0":
            out[position] = "0"
            spare -= 1
    return "".join(out)

# Clause main [Confidence: 1.00]
def main():
    n, k, s = read_input()
    sys.stdout.write(smallest_value(n, k, s) + "\n")


if __name__ == "__main__":
    main()

