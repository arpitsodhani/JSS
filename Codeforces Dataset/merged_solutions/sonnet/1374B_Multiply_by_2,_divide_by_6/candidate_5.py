import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[i]) for i in range(1, t + 1)]


# --- clause: moves_needed :: (n: int) -> int ---
def moves_needed(n):
    moves = 0
    while n != 1:
        if n % 6:
            if n % 3:
                return -1
            n *= 2
        else:
            n //= 6
        moves += 1
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(str(moves_needed(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
