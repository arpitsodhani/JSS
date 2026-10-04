import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: split_candies :: (n: int) -> list[int] ---
def split_candies(n):
    gifts = []
    used = 0
    piece = 1
    while used + piece <= n:
        gifts.append(piece)
        used += piece
        piece += 1
    if used < n:
        gifts[-1] += n - used
    return gifts

# --- clause: main :: () -> None ---
def main():
    n = read_input()
    gifts = split_candies(n)
    sys.stdout.write(str(len(gifts)) + "\n" + " ".join(map(str, gifts)) + "\n")


if __name__ == "__main__":
    main()
