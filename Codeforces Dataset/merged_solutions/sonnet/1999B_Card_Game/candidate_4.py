import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append(tuple(numbers[1 + 4 * i:5 + 4 * i]))
    return cases


# --- clause: count_wins :: (a1: int, a2: int, b1: int, b2: int) -> int ---
def count_wins(a1, a2, b1, b2):
    mine = [a1, a2]
    theirs = [b1, b2]
    wins = 0
    for first in (0, 1):
        for second in (0, 1):
            rounds = 0
            if mine[first] > theirs[second]:
                rounds += 1
            if mine[first] < theirs[second]:
                rounds -= 1
            if mine[1 - first] > theirs[1 - second]:
                rounds += 1
            if mine[1 - first] < theirs[1 - second]:
                rounds -= 1
            if rounds > 0:
                wins += 1
    return wins


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a1, a2, b1, b2 in read_input():
        pieces.append(count_wins(a1, a2, b1, b2))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
