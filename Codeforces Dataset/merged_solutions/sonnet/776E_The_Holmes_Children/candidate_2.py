import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# --- clause: totient :: (value: int) -> int ---
def totient(value):
    result = value
    if value % 2 == 0:
        result -= result // 2
        while value % 2 == 0:
            value //= 2
    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            result -= result // factor
            while value % factor == 0:
                value //= factor
        factor += 2
    if value > 1:
        result -= result // value
    return result

# --- clause: iterate_totient :: (n: int, k: int) -> int ---
def iterate_totient(n, k):
    steps = (k + 1) // 2
    value = n
    while steps and value > 1:
        value = totient(value)
        steps -= 1
    return value % 1000000007

# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write(str(iterate_totient(n, k)) + "\n")


if __name__ == "__main__":
    main()
