import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    numbers = data[1:]
    rows = []
    for i in range(n):
        rows.append((int(numbers[3 * i + 1]), int(numbers[3 * i + 2])))
    return rows

# Clause good_contest [Confidence: 0.40]
def good_contest(rows):
    for before, after in rows:
        if before >= 2400 and after > before:
            return "YES"
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(good_contest(read_input()) + "\n")


if __name__ == "__main__":
    main()

