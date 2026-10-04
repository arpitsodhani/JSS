import sys


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    return n, k, data[2]


# --- clause: best_coins :: (n: int, k: int, cards: bytes) -> int ---
def best_coins(n, k, cards):
    counts = [0] * 26
    for ch in cards:
        counts[ch - 65] += 1
    counts.sort(reverse=True)
    total = 0
    left = k
    index = 0
    while left > 0 and index < 26:
        take = min(counts[index], left)
        total += take * take
        left -= take
        index += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, cards = read_input()
    print(best_coins(n, k, cards))


if __name__ == "__main__":
    main()
