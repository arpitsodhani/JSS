import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: count_moves :: (p: list[int]) -> int ---
def count_moves(p):
    n = len(p)
    spot = [0] * (n + 2)
    for i in range(n):
        spot[p[i]] = i
    moves = 0
    for element in range(1, n):
        if spot[element + 1] < spot[element]:
            moves += 1
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for p in read_input():
        out.append(count_moves(p))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
