import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: grow :: (n: int, k: int) -> int ---
def grow(n, k):
    steps = k
    while steps and n % 2:
        d = 2
        while d * d <= n and n % d:
            d += 1
        n += d if d * d <= n else n
        steps -= 1
    return n + 2 * steps


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, k in read_input():
        pieces.append(grow(n, k))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
