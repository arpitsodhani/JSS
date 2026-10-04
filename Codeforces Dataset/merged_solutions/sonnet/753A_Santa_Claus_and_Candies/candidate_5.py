import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: split_candies :: (n: int) -> list[int] ---
def split_candies(n):
    gifts = []
    left = n
    piece = 1
    while left >= piece:
        gifts.append(piece)
        left -= piece
        piece += 1
    if left:
        gifts[-1] += left
    return gifts

# --- clause: main :: () -> None ---
def main():
    n = read_input()
    gifts = split_candies(n)
    sys.stdout.write(str(len(gifts)) + "\n" + " ".join(map(str, gifts)) + "\n")


if __name__ == "__main__":
    main()
