import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()

# Clause find_source [Confidence: 1.00]
def find_source(text):
    total = len(text)
    for size in range((total + 2) // 2, total):
        overlap = 2 * size - total
        if overlap < 1 or overlap >= size:
            continue
        if text[:size] == text[total - size:]:
            return "YES\n" + text[:size]
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(find_source(read_input()) + "\n")


if __name__ == "__main__":
    main()

