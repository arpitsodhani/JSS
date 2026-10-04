import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: exact_root :: (value: int) -> int ---
def exact_root(value):
    guess = int(value ** 0.5)
    while guess * guess > value:
        guess -= 1
    while (guess + 1) * (guess + 1) <= value:
        guess += 1
    return guess


# --- clause: build_test :: (x: int) -> tuple[int, int] | None ---
def build_test(x):
    for d in range(1, 100001):
        total = x + d * d
        n = exact_root(total)
        if n * n != total:
            continue
        if n < d or n < 1:
            continue
        m = n // d
        if m >= 1 and n // m == d:
            return n, m
    return None


# --- clause: main :: () -> None ---
def main():
    out = []
    for x in read_input():
        found = build_test(x)
        out.append("-1" if found is None else "%d %d" % found)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
