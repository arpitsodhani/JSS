import sys


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, data[2]


# --- clause: best_coins :: (n: int, k: int, cards: bytes) -> int ---
def best_coins(n, k, cards):
    counts = [0] * 26
    for ch in cards[:n]:
        counts[ch - 65] += 1
    counts.sort(reverse=True)
    total = 0
    left = k
    for size in counts:
        if left == 0:
            break
        take = left if left < size else size
        total += take * take
        left -= take
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, cards = read_input()
    sys.stdout.write(str(best_coins(n, k, cards)) + "\n")


if __name__ == "__main__":
    main()
