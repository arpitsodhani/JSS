import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


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
    d = 1
    while d * d <= x + d * d and d <= 100000:
        total = x + d * d
        n = exact_root(total)
        if n * n == total and n >= 1 and d <= n:
            m = n // d
            if m >= 1 and n // m == d:
                return n, m
        d += 1
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
