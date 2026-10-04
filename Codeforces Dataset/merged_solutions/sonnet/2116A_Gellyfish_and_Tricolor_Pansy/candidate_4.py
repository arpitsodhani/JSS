import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append(tuple(numbers[1 + 4 * i:5 + 4 * i]))
    return cases


# --- clause: winner :: (a: int, b: int, c: int, d: int) -> str ---
def winner(a, b, c, d):
    mine = min(a, c)
    theirs = min(b, d)
    if mine < theirs:
        return "Flower"
    return "Gellyfish"


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a, b, c, d in read_input():
        pieces.append(winner(a, b, c, d))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
