import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: smallest_peak :: (n: int, k: int) -> int ---
def smallest_peak(n, k):
    amount = ((n + k - 1) // k) * k
    return (amount + n - 1) // n


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(smallest_peak(n, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
