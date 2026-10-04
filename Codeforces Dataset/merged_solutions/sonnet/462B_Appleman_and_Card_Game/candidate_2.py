import sys


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    n, k, cards = int(data[0]), int(data[1]), data[2]
    return n, k, cards


# --- clause: best_coins :: (n: int, k: int, cards: bytes) -> int ---
def best_coins(n, k, cards):
    counts = [0] * 26
    for ch in cards:
        counts[ch - 65] = counts[ch - 65] + 1
    counts = sorted(counts, reverse=True)
    total = 0
    left = k
    for size in counts:
        if left == 0:
            break
        take = size if size < left else left
        total += take * take
        left -= take
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, cards = read_input()
    sys.stdout.write("%d\n" % best_coins(n, k, cards))


if __name__ == "__main__":
    main()
