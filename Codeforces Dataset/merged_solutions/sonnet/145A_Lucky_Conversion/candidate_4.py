import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[0].decode(), numbers[1].decode()


# --- clause: fewest_moves :: (a: str, b: str) -> int ---
def fewest_moves(a, b):
    fours_a = 0
    fours_b = 0
    same = 0
    for i in range(len(a)):
        if a[i] == "4":
            fours_a += 1
        if b[i] == "4":
            fours_b += 1
        if a[i] == b[i]:
            same += 1
    gap = fours_a - fours_b
    if gap < 0:
        gap = -gap
    wrong = len(a) - same
    return gap + (wrong - gap) // 2


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % fewest_moves(a, b))


if __name__ == "__main__":
    main()
