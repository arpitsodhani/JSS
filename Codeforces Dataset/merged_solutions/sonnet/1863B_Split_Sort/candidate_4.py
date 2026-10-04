import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: count_moves :: (p: list[int]) -> int ---
def count_moves(p):
    n = len(p)
    spot = {}
    for i in range(n):
        spot[p[i]] = i
    moves = 0
    value = 1
    while value < n:
        if spot[value] > spot[value + 1]:
            moves += 1
        value += 1
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for p in read_input():
        out.append(count_moves(p))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
