import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: grow :: (n: int, k: int) -> int ---
def grow(n, k):
    if n % 2:
        d = 3
        smallest = n
        while d * d <= n:
            if n % d == 0:
                smallest = d
                break
            d += 2
        n += smallest
        k -= 1
    return n + 2 * k


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, k in read_input():
        lines.append(grow(n, k))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
