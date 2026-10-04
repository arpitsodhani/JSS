import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    b, k = int(data[0]), int(data[1])
    digits = [int(token) for token in data[2:k + 2]]
    return b, k, digits


# --- clause: parity :: (b: int, k: int, digits: list[int]) -> str ---
def parity(b, k, digits):
    if b % 2 == 0:
        rest = digits[k - 1] % 2
    else:
        rest = 0
        for value in digits:
            rest = (rest + value) % 2
    if rest:
        return "odd"
    return "even"


# --- clause: main :: () -> None ---
def main():
    b, k, digits = read_input()
    print(parity(b, k, digits))


if __name__ == "__main__":
    main()
