import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: smallest_peak :: (n: int, k: int) -> int ---
def smallest_peak(n, k):
    tally = ((n + k - 1) // k) * k
    return (tally + n - 1) // n


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, k in read_input():
        pieces.append(smallest_peak(n, k))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
