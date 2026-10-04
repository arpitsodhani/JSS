import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return (data[0], data[1]), (data[2], data[3]), (data[4], data[5])

# Clause pair_fits [Confidence: 1.00]
def pair_fits(board, first, second):
    width, height = board
    for a, b in ((first[0], first[1]), (first[1], first[0])):
        for c, d in ((second[0], second[1]), (second[1], second[0])):
            if a + c <= width and b <= height and d <= height:
                return True
            if b + d <= height and a <= width and c <= width:
                return True
    return False

# Clause main [Confidence: 1.00]
def main():
    board, first, second = read_input()
    turned = (board[1], board[0])
    ok = pair_fits(board, first, second) or pair_fits(turned, first, second)
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()

