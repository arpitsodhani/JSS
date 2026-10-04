import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2]


# --- clause: bar_state :: (n: int, k: int, t: int) -> list[int] ---
def bar_state(n, k, t):
    running = t * n * k // 100
    full = running // k
    squares = []
    for i in range(n):
        if i < full:
            squares.append(k)
        elif i == full:
            squares.append(running - full * k)
        else:
            squares.append(0)
    return squares


# --- clause: main :: () -> None ---
def main():
    n, k, t = read_input()
    sys.stdout.write(" ".join(map(str, bar_state(n, k, t))) + "\n")


if __name__ == "__main__":
    main()
