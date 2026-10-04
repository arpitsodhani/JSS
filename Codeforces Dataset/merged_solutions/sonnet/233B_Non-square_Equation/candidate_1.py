import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: exact_root :: (value: int) -> int ---
def exact_root(value):
    guess = int(value ** 0.5)
    while guess * guess > value:
        guess -= 1
    while (guess + 1) * (guess + 1) <= value:
        guess += 1
    return guess


# --- clause: smallest_root :: (n: int) -> int ---
def smallest_root(n):
    best = -1
    for s in range(1, 200):
        root = exact_root(s * s + 4 * n)
        if root * root != s * s + 4 * n:
            continue
        if (root - s) % 2:
            continue
        x = (root - s) // 2
        if x <= 0:
            continue
        digits = 0
        value = x
        while value:
            digits += value % 10
            value //= 10
        if digits == s and (best < 0 or x < best):
            best = x
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % smallest_root(read_input()))


if __name__ == "__main__":
    main()
