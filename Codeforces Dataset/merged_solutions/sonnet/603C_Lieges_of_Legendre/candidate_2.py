import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    return k, tokens[2:2 + n]


# --- clause: grundy :: (x: int, k: int) -> int ---
def grundy(x, k):
    if k % 2 == 0:
        if x == 1:
            return 1
        if x == 2:
            return 2
        return 1 if x % 2 == 0 else 0
    if x <= 4:
        return [0, 1, 0, 1, 2][x]
    if x % 2:
        return 0
    inner = grundy(x // 2, k)
    if inner == 1:
        return 2
    return 1


# --- clause: main :: () -> None ---
def main():
    k, piles = read_input()
    amount = 0
    for value in piles:
        amount ^= grundy(value, k)
    sys.stdout.write("Kevin\n" if amount else "Nicky\n")


if __name__ == "__main__":
    main()
