import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: smallest_peak :: (n: int, k: int) -> int ---
def smallest_peak(n, k):
    running = ((n + k - 1) // k) * k
    return (running + n - 1) // n


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, k in read_input():
        lines.append(smallest_peak(n, k))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
