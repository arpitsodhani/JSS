import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# --- clause: totient :: (value: int) -> int ---
def totient(value):
    result = value
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            while value % factor == 0:
                value //= factor
            result -= result // factor
        factor += 1
    if value > 1:
        result -= result // value
    return result

# --- clause: iterate_totient :: (n: int, k: int) -> int ---
def iterate_totient(n, k):
    rounds = k - k // 2
    value = n
    for _ in range(rounds):
        if value <= 1:
            break
        value = totient(value)
    return value % 1000000007

# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write(str(iterate_totient(n, k)) + "\n")


if __name__ == "__main__":
    main()
