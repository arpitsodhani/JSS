import sys


# --- clause: read_input :: () -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return (numbers[0], numbers[1]), (numbers[2], numbers[3]), (numbers[4], numbers[5])


# --- clause: pair_fits :: (board: tuple[int, int], first: tuple[int, int], second: tuple[int, int]) -> bool ---
def pair_fits(board, first, second):
    width, height = board
    turns = [(first, second), ((first[1], first[0]), second),
             (first, (second[1], second[0])), ((first[1], first[0]), (second[1], second[0]))]
    for one, two in turns:
        if one[0] + two[0] <= width and max(one[1], two[1]) <= height:
            return True
        if one[1] + two[1] <= height and max(one[0], two[0]) <= width:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    board, first, second = read_input()
    turned = (board[1], board[0])
    ok = pair_fits(board, first, second) or pair_fits(turned, first, second)
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
