import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: smallest_peak :: (n: int, k: int) -> int ---
def smallest_peak(n, k):
    blocks = n // k
    if n % k:
        blocks += 1
    total = blocks * k
    spread = total // n
    if total % n:
        spread += 1
    return spread


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(smallest_peak(n, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
