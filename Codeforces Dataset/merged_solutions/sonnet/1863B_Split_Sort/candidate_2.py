import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: count_moves :: (p: list[int]) -> int ---
def count_moves(p):
    n = len(p)
    spot = [0] * (n + 2)
    for i in range(n):
        spot[p[i]] = i
    moves = 0
    for item in range(1, n):
        if spot[item + 1] < spot[item]:
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
