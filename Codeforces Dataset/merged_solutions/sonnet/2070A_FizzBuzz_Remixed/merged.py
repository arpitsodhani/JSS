import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause fizzbuzz_count [Confidence: 0.80]
def fizzbuzz_count(n):
    whole = n // 15
    rest = n % 15
    return whole * 3 + (rest + 1 if rest < 2 else 3)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        collected.append(fizzbuzz_count(n))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

