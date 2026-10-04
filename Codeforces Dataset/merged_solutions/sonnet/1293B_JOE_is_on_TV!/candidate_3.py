import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    return count


# --- clause: best_prize :: (n: int) -> float ---
def best_prize(n):
    total = 0.0
    opponents = 1
    while opponents <= n:
        total += 1.0 / opponents
        opponents += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("{:.12f}\n".format(best_prize(n)))


if __name__ == "__main__":
    main()
