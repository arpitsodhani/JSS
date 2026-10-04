import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: least_sum :: (x: list[int]) -> int ---
def least_sum(x):
    base = x[0]
    for number in x:
        base = gcd_of(base, number)
    return base * len(x)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_sum(read_input()))


if __name__ == "__main__":
    main()
