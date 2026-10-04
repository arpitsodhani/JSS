import sys


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, bytes(data[2])


# --- clause: best_coins :: (n: int, k: int, cards: bytes) -> int ---
def best_coins(n, k, cards):
    counts = [0] * 26
    for ch in cards:
        counts[ch - 65] += 1
    counts.sort()
    counts.reverse()
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
    answer = best_coins(n, k, cards)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
