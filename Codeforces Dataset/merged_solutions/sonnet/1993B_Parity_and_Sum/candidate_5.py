import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: fewest_moves :: (a: list[int]) -> int ---
def fewest_moves(a):
    evens = sorted(value for value in a if value % 2 == 0)
    odds = [value for value in a if value % 2]
    if not evens or not odds:
        return 0
    largest = max(odds)
    moves = 0
    for value in evens:
        if largest < value:
            return len(evens) + 1
        largest = largest + value
        moves = moves + 1
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(fewest_moves(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
