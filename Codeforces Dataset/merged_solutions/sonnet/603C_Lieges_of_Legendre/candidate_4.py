import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: grundy :: (x: int, k: int) -> int ---
def grundy(x, k):
    if k % 2 == 0:
        if x <= 2:
            return x
        return 1 - x % 2
    small = [0, 1, 0, 1, 2]
    while x > 4:
        if x % 2:
            return 0
        x //= 2
        if grundy(x, k) == 1:
            return 2
        return 1
    return small[x]


# --- clause: main :: () -> None ---
def main():
    k, piles = read_input()
    summed = 0
    for value in piles:
        summed ^= grundy(value, k)
    sys.stdout.write("Kevin\n" if summed else "Nicky\n")


if __name__ == "__main__":
    main()
