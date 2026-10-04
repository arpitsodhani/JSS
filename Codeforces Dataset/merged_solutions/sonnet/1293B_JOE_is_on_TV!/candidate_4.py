import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: best_prize :: (n: int) -> float ---
def best_prize(n):
    total = 0.0
    for opponents in range(1, n + 1):
        total = total + 1.0 / opponents
    return total


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    prize = best_prize(n)
    sys.stdout.write("%.12f\n" % prize)


if __name__ == "__main__":
    main()
