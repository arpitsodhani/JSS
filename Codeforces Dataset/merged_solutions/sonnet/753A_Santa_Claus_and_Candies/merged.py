import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause split_candies [Confidence: 0.60]
def split_candies(n):
    gifts = []
    left = n
    piece = 1
    while left >= piece:
        gifts.append(piece)
        left -= piece
        piece += 1
    if left:
        gifts[-1] += left
    return gifts

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    gifts = split_candies(n)
    sys.stdout.write(str(len(gifts)) + "\n" + " ".join(map(str, gifts)) + "\n")


if __name__ == "__main__":
    main()

