import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: count_moves :: (p: list[int]) -> int ---
def count_moves(p):
    n = len(p)
    spot = [0] * (n + 2)
    for i in range(n):
        spot[p[i]] = i
    moves = 0
    for number in range(1, n):
        if spot[number + 1] < spot[number]:
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
