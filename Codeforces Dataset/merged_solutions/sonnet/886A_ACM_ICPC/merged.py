import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return list(map(int, sys.stdin.buffer.read().split()))[:6]

# Clause can_split [Confidence: 1.00]
def can_split(scores):
    amount = sum(scores)
    if amount % 2:
        return False
    half = amount // 2
    for i in range(6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                if scores[i] + scores[j] + scores[k] == half:
                    return True
    return False

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("YES\n" if can_split(read_input()) else "NO\n")


if __name__ == "__main__":
    main()

