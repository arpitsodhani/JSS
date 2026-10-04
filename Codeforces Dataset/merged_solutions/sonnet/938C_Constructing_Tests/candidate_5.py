import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


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
        running = x + d * d
        n = exact_root(running)
        if n * n == running and n >= 1 and d <= n:
            m = n // d
            if m >= 1 and n // m == d:
                return n, m
        d += 1
    return None


# --- clause: main :: () -> None ---
def main():
    out = []
    for x in read_input():
        hit = build_test(x)
        out.append("-1" if hit is None else "%d %d" % hit)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
