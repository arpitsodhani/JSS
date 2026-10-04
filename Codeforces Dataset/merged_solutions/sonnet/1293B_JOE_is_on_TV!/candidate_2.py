import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n


# --- clause: best_prize :: (n: int) -> float ---
def best_prize(n):
    total = 0.0
    for opponents in range(n, 0, -1):
        total += 1.0 / opponents
    return total


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    print("%.12f" % best_prize(n))


if __name__ == "__main__":
    main()
