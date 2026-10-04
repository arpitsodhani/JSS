import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    b = int(data[0])
    k = int(data[1])
    digits = [int(data[i + 2]) for i in range(k)]
    return b, k, digits


# --- clause: parity :: (b: int, k: int, digits: list[int]) -> str ---
def parity(b, k, digits):
    if not b % 2:
        rest = digits[k - 1] & 1
    else:
        rest = 0
        for value in digits:
            rest ^= value % 2
    if rest:
        return "odd"
    return "even"


# --- clause: main :: () -> None ---
def main():
    b, k, digits = read_input()
    answer = parity(b, k, digits)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
