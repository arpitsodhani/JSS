import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_word [Confidence: 1.00]
def build_word(n):
    vowels = "aeiou"
    pieces = []
    for i in range(5):
        times = n // 5 + (1 if i < n % 5 else 0)
        pieces.append(vowels[i] * times)
    return "".join(pieces)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        collected.append(build_word(n))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

