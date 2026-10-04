import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: bar_state :: (n: int, k: int, t: int) -> list[int] ---
def bar_state(n, k, t):
    total = t * n * k // 100
    full = total // k
    squares = [k] * full
    if full < n:
        squares.append(total - full * k)
        squares.extend([0] * (n - full - 1))
    return squares


# --- clause: main :: () -> None ---
def main():
    n, k, t = read_input()
    sys.stdout.write(" ".join(map(str, bar_state(n, k, t))) + "\n")


if __name__ == "__main__":
    main()
