import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), data[1]

# Clause totient [Confidence: 1.00]
def totient(value):
    result = value
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            while value % factor == 0:
                value //= factor
            result -= result // factor
        factor += 1
    if value > 1:
        result -= result // value
    return result

# Clause count_shifts [Confidence: 0.80]
def count_shifts(n, bits):
    total = 0
    for step in range(1, n + 1):
        if n % step:
            continue
        parity = [0] * step
        for i in range(n):
            parity[i % step] ^= bits[i] - 48
        good = True
        for value in parity:
            if value:
                good = False
                break
        if good:
            total += totient(n // step)
    return total

# Clause main [Confidence: 1.00]
def main():
    n, bits = read_input()
    sys.stdout.write(str(count_shifts(n, bits)) + "\n")


if __name__ == "__main__":
    main()

