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


# --- clause: raise_to_powers :: (a: list[int]) -> list[tuple[int, int]] ---
def raise_to_powers(a):
    moves = []
    index = 0
    for value in a:
        index += 1
        target = 1 << (value - 1).bit_length() if value > 1 else 1
        moves.append((index, target - value))
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        moves = raise_to_powers(a)
        out.append(str(len(moves)))
        for index, add in moves:
            out.append(str(index) + " " + str(add))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
