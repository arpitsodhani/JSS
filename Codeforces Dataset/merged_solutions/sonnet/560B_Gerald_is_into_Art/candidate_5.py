import sys


# --- clause: read_input :: () -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return (raw[0], raw[1]), (raw[2], raw[3]), (raw[4], raw[5])


# --- clause: pair_fits :: (board: tuple[int, int], first: tuple[int, int], second: tuple[int, int]) -> bool ---
def pair_fits(board, first, second):
    width, height = board
    for a, b in ((first[0], first[1]), (first[1], first[0])):
        for c, d in ((second[0], second[1]), (second[1], second[0])):
            if a + c <= width and b <= height and d <= height:
                return True
            if b + d <= height and a <= width and c <= width:
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
